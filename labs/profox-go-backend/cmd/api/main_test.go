package main

import (
 "net/http"
 "net/http/httptest"
 "testing"
)

func TestHealth(t *testing.T) {
 req := httptest.NewRequest(http.MethodGet, "/healthz", nil)
 rec := httptest.NewRecorder()
 (App{}).routes().ServeHTTP(rec, req)
 if rec.Code != http.StatusOK { t.Fatalf("got %d", rec.Code) }
}
