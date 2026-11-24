import hashlib
from pathlib import Path, PurePosixPath
import tempfile
import zipfile
import stat

def hash_arquivo(p):
    with Path(p).open("rb") as f:
        return hashlib.file_digest(f, "sha256").hexdigest()

def backup(origem, arquivo):
    origem = Path(origem)
    with zipfile.ZipFile(arquivo, "w", zipfile.ZIP_DEFLATED) as z:
        for p in sorted(origem.rglob("*")):
            if p.is_symlink():
                raise ValueError("Link nao permitido")
            if p.is_file():
                z.write(p, p.relative_to(origem).as_posix())
    return hash_arquivo(arquivo)

def restaurar(arquivo, destino, esperado):
    if hash_arquivo(arquivo) != esperado:
        raise ValueError("Hash divergente")
    destino = Path(destino)
    if destino.exists():
        raise ValueError("Destino deve ser novo")
    with zipfile.ZipFile(arquivo) as z:
        nomes = set()
        for i in z.infolist():
            p = PurePosixPath(i.filename)
            if p.is_absolute() or ".." in p.parts or "\\" in i.filename or not p.parts or ":" in i.filename or i.is_dir() or stat.S_ISLNK(i.external_attr >> 16) or p in nomes:
                raise ValueError("Entrada insegura")
            nomes.add(p)
        if any(parent in nomes for p in nomes for parent in p.parents):
            raise ValueError("Colisao arquivo/diretorio")
        destino.mkdir()
        for i in z.infolist():
            p = destino.joinpath(*PurePosixPath(i.filename).parts)
            p.parent.mkdir(parents=True, exist_ok=True)
            with z.open(i) as src, p.open("xb") as out:
                import shutil
                shutil.copyfileobj(src, out)

if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as t:
        p = Path(t)
        (p/"origem").mkdir()
        (p/"origem"/"demo.txt").write_text("Dados ficticios")
        h = backup(p/"origem", p/"backup.zip")
        restaurar(p/"backup.zip", p/"restaurado", h)
        assert hash_arquivo(p/"origem"/"demo.txt") == hash_arquivo(p/"restaurado"/"demo.txt")
        print("Backup restaurado e integridade confirmada")
