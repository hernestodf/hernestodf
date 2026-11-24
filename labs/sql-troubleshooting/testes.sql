BEGIN;
UPDATE chamados SET status='aberto' WHERE id=1;
ROLLBACK;
DO $$
BEGIN
  IF (SELECT count(*) FROM chamados WHERE status='aberto') <> 100 THEN
    RAISE EXCEPTION 'Contagem incorreta ou rollback falhou';
  END IF;
  IF NOT EXISTS (SELECT 1 FROM pg_indexes WHERE indexname='idx_chamados_status') THEN
    RAISE EXCEPTION 'Indice ausente';
  END IF;
END $$;
