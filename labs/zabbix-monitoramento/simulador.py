"""Modelo didático de alerta; não integra com Zabbix."""
def estado_alerta(amostras, limite=3):
    if type(limite) is not int or limite < 1:
        raise ValueError("Limite deve ser inteiro positivo")
    falhas = 0
    for amostra in amostras:
        if type(amostra) is not bool:
            raise ValueError("Amostra deve ser booleana")
        falhas = 0 if amostra else falhas + 1
    return "PROBLEMA" if falhas >= limite else "OK"
