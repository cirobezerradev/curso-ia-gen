def analise_estoque(qtd_estoque: int, estoque_min: int) -> None:

    if qtd_estoque <= estoque_min:
        print('\nSituação: AVALIAR REPOSIÇÃO')
    else:
        print('\nSituação: '\
        'estoque acima do mínimo. Manter acompanhamento.')

    return None

qtd_estoque = int(input('Quantidade em Estoque: '))
estoque_min = int(input('Estoque mínimo: '))


analise_estoque(qtd_estoque, estoque_min)