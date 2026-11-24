from pathlib import Path
import stat
import json
def auditar(texto, modo):
    cfg = {}
    for linha in texto.splitlines():
        partes = linha.split('#', 1)[0].split()
        if len(partes) == 2:
            cfg.setdefault(partes[0].lower(), partes[1].lower())
    return {
        'root_desativado': cfg.get('permitrootlogin') == 'no',
        'senha_desativada': cfg.get('passwordauthentication') == 'no',
        'arquivo_restrito': modo & 0o077 == 0,
    }
if __name__ == '__main__':
    p = Path(__file__).with_name('sshd-demo.conf')
    print(json.dumps(auditar(p.read_text(), stat.S_IMODE(p.stat().st_mode)), indent=2))
