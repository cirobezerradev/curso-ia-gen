# EXERCÍCIO 4
def analise_tx_conversao(contatos_gerados: int, convertidos: int)-> print:

    if contatos_gerados == 0:
        return print('Nenhum contato gerado: não é possível calcular a taxa.')
    elif convertidos > contatos_gerados:
        return print('Dados de insersão inconsistente! Insira dados consistentes.')
    else:
        tx_conversao = convertidos / contatos_gerados * 100
        print(f'Taxa de converção: {tx_conversao:.2f}%')


    if tx_conversao >= 20:
        return print('Classificação: EXCELENTE')
    elif tx_conversao >= 10 and tx_conversao <= 19.9:
        return print('Classificação: SATISFATÓRIO')



contatos_gerados = int(input('Contatos gerados pela campanha: '))
convertidos = int(input('Contatos convertidos em oportunidades: '))

analise_tx_conversao(contatos_gerados, convertidos)

