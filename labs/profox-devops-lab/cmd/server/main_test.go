package main

import (
 "net/http"
 "net/http/httptest"
 "testing"
)

func TestHealth(t *testing.T) {
 req := httptest.NewRequest(http.MethodGet, "/healthz", nil)
 rec := httptest.NewRecorder()
 handler().ServeHTTP(rec, req)
 if rec.Code != http.StatusOK { t.Fatalf("status: %d", rec.Code) }
 if rec.Body.String() != "{\"status\":\"ok\"}\n" { t.Fatalf("body: %s", rec.Body.String()) }
}
