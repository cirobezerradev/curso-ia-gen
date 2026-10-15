produtos = ['Motor Eletrico', 'Sensor indutivo', 'Correia dentada',
'Rolamento 6205', 'Contator 25A']

novo_produto = 'Válvula Solenoide'

print('Produtos cadastrados:')

for produto in produtos:
    print(produto)

print(f'Quantidade de produtos: {len(produtos)}')
print(f'Primeiro produto: {produto[0]}')
print(f'Último produto: {produto[-1]}')

produtos.append(novo_produto)

print('Lista atualizada:')
for produto in produtos:
    print(produto)

print(f'Quantidade de atual: {len(produtos)}')
