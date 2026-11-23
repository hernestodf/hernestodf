package main

import (
 "context"
 "database/sql"
 "encoding/json"
 "errors"
 "log"
 "net/http"
 "os"
 "strings"
 "time"

 _ "github.com/jackc/pgx/v5/stdlib"
)

type Task struct { ID int64 `json:"id"`; Title string `json:"title"` }
type App struct { DB *sql.DB }

func (a App) routes() http.Handler {
 mux := http.NewServeMux()
 mux.HandleFunc("GET /healthz", func(w http.ResponseWriter, r *http.Request) {
  w.Header().Set("Content-Type", "application/json")
  _ = json.NewEncoder(w).Encode(map[string]string{"status":"ok"})
 })
 mux.HandleFunc("GET /tasks", func(w http.ResponseWriter, r *http.Request) {
  rows, err := a.DB.QueryContext(r.Context(), "SELECT id, title FROM tasks ORDER BY id DESC LIMIT 100")
  if err != nil { http.Error(w, "database error", 500); return }
  defer rows.Close()
  tasks := make([]Task, 0)
  for rows.Next() {
   var t Task
   if err := rows.Scan(&t.ID, &t.Title); err != nil { http.Error(w, "database error", 500); return }
   tasks = append(tasks, t)
  }
  if err := rows.Err(); err != nil { http.Error(w, "database error", 500); return }
  w.Header().Set("Content-Type", "application/json")
  _ = json.NewEncoder(w).Encode(tasks)
 })
 mux.HandleFunc("POST /tasks", func(w http.ResponseWriter, r *http.Request) {
  r.Body = http.MaxBytesReader(w, r.Body, 4096)
  var input struct { Title string `json:"title"` }
  if err := json.NewDecoder(r.Body).Decode(&input); err != nil { http.Error(w, "invalid JSON", 400); return }
  input.Title = strings.TrimSpace(input.Title)
  if input.Title == "" || len(input.Title) > 120 { http.Error(w, "title must have 1-120 bytes", 400); return }
  var task Task
  err := a.DB.QueryRowContext(r.Context(), "INSERT INTO tasks(title) VALUES ($1) RETURNING id, title", input.Title).Scan(&task.ID, &task.Title)
  if err != nil { http.Error(w, "database error", 500); return }
  w.Header().Set("Content-Type", "application/json")
  w.WriteHeader(http.StatusCreated)
  _ = json.NewEncoder(w).Encode(task)
 })
 return mux
}

func main() {
 dsn := os.Getenv("DATABASE_URL")
 if dsn == "" { log.Fatal("DATABASE_URL required") }
 db, err := sql.Open("pgx", dsn)
 if err != nil { log.Fatal(err) }
 defer db.Close()
 ctx, cancel := context.WithTimeout(context.Background(), 30*time.Second)
 defer cancel()
 for {
  if err = db.PingContext(ctx); err == nil { break }
  if errors.Is(ctx.Err(), context.DeadlineExceeded) { log.Fatal(err) }
  time.Sleep(time.Second)
 }
 port := os.Getenv("PORT"); if port == "" { port = "8080" }
 srv := &http.Server{Addr: ":"+port, Handler: App{DB:db}.routes(), ReadHeaderTimeout: 5*time.Second}
 log.Fatal(srv.ListenAndServe())
}
