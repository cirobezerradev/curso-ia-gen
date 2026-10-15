
vendas = [9500.00, 12300.00, 10000.00, 11750.50, 8200.00]

print('Vendas registradas:')
for venda in vendas:
    print(f'R$ {venda:.2f}')

print(f'\nTotal da semana: {sum(vendas):.2f}')
print(f'Média diária: {sum(vendas) / len(vendas):.2f}')
print(f'Maior venda: {max(vendas):.2f}')
print(f'Menor venda: {min(vendas):.2f}')

