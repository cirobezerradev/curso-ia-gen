def calcular_aprovadas(produzidas: int, rejeitadas: int)-> str:
    try:
        if produzidas <= 0:
            raise ValueError('O número de peças produzidas não pode ser zero.')
        elif rejeitadas < 0:
            raise ValueError('O número de peças rejeitadas não pode ser negativo.')
        elif rejeitadas > produzidas:
            raise ValueError('O número de peças rejeitadas não pode ser maior que o número de peças produzidas.')

        calculo = produzidas - rejeitadas
        return f'Peças Aprovadas: {calculo}'

    except ValueError as e:
        return f'Erro: {e}'
 
    

produzidas = int(input('Peças Produzidas: '))
rejeitadas = int(input('Peças Rejeitadas: '))

print(calcular_aprovadas(produzidas, rejeitadas))