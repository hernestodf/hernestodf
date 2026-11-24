CREATE TABLE IF NOT EXISTS chamados (
  id integer PRIMARY KEY,
  status text NOT NULL CHECK (status IN ('aberto','fechado')),
  assunto text NOT NULL
);
INSERT INTO chamados SELECT n, CASE WHEN n % 100 = 0 THEN 'aberto' ELSE 'fechado' END, 'Chamado ficticio ' || n FROM generate_series(1,10000) n ON CONFLICT DO NOTHING;
ANALYZE chamados;
EXPLAIN SELECT * FROM chamados WHERE status='aberto';
CREATE INDEX IF NOT EXISTS idx_chamados_status ON chamados(status);
ANALYZE chamados;
EXPLAIN (ANALYZE, BUFFERS) SELECT * FROM chamados WHERE status='aberto';
