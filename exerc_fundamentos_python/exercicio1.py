# EXERCÍCIO 1

def relatorio_estoque(nome_produto: str, qtd_estoque: int, valor_unit: float) -> print:
    vr_estoque: float = qtd_estoque * valor_unit 

    relatorio = f'''
=== VALORIZAÇÃO DE ESTOQUE ===
Nome do produto: {nome_produto}
Quantidade disponível: {qtd_estoque}
Preço unitário: R$ {valor_unit:.2f}
\n
------ RELATÓRIO ------
Produto: {nome_produto}
Quantidade: {qtd_estoque} unidades
Preço unitário: R$ {valor_unit:.2f}
Valor total em estoque: R$ {vr_estoque:.2f}
'''
    
    return print(relatorio)


nome_produto: str = input('Digite o nome do produto: ')
qtd_estoque: int = int(input('Digite a quantidade disponível: '))
valor_unit: float = float(input('Digite o valor unitário: '))

relatorio_estoque(nome_produto, qtd_estoque, valor_unit)