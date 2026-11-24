import json
from pathlib import Path
def validar(plano):
    ids = set()
    total = 0
    for vm in plano['instancias']:
        ident = vm['id']
        if type(ident) is not int or ident < 100 or ident in ids:
            raise ValueError('ID invalido ou duplicado')
        ids.add(ident)
        ram = vm['ram_mib']
        if type(ram) is not int or ram <= 0:
            raise ValueError('RAM invalida')
        total += ram
    if total > plano['ram_disponivel_mib']:
        raise ValueError('Capacidade excedida')
    return total
if __name__ == '__main__':
    plano = json.loads(Path(__file__).with_name('plano.json').read_text())
    print('RAM planejada:', validar(plano), 'MiB')
