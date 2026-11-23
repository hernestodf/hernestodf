package main

import (
 "encoding/json"
 "log"
 "net/http"
 "os"
 "time"
)

func handler() http.Handler {
 mux := http.NewServeMux()
 mux.HandleFunc("GET /healthz", func(w http.ResponseWriter, r *http.Request) {
  w.Header().Set("Content-Type", "application/json")
  _ = json.NewEncoder(w).Encode(map[string]string{"status":"ok"})
 })
 mux.HandleFunc("GET /readyz", func(w http.ResponseWriter, r *http.Request) {
  w.WriteHeader(http.StatusNoContent)
 })
 return mux
}

func main() {
 port := os.Getenv("PORT")
 if port == "" { port = "8080" }
 srv := &http.Server{Addr: ":" + port, Handler: handler(), ReadHeaderTimeout: 5 * time.Second}
 log.Printf("listening on :%s", port)
 log.Fatal(srv.ListenAndServe())
}
