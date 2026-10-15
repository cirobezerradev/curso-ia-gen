codigo_produto = input('Digite Código do Produto: ')

codigo_produto = codigo_produto.strip().upper()

if len(codigo_produto) == 0:
    print('Nenhum Código Informado')
else:    
    print(f'Código Padronizado: {codigo_produto}')
    print(f'Comprimento: {len(codigo_produto)}')

