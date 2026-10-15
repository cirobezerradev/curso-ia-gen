# EXERCÍCIO 2

def relatorio_meta(vr_vendas: float, meta: float)-> print:
    diferenca_meta: float = vr_vendas - meta

    if diferenca_meta < 0:
        resultado = f'meta NÃO atingida. Faltaram {-(diferenca_meta):.2f}'
    else:
        resultado = 'META ATINGIDA'

    relatorio_meta = f'''
Vendas do período: R$ {vr_vendas:.2f}
Meta estabelecida: R$ {meta:.2f}
Diferença em relação à meta: R$ {diferenca_meta:.2f}
Resultado: {resultado}.
'''
    return print(relatorio_meta)

vr_vendas = float(input('Valor de vendas do período: '))
meta = float(input('Meta estabelecida: '))

relatorio_meta(vr_vendas, meta)