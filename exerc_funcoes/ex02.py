def calcular_custo(quantidade: int, custo_unitario: float = 8.50) -> float:
    try:
        calculo: float = quantidade * custo_unitario
        return f'{calculo:.2f}'
    
    except Exception as e:
        return f'Erro: {e}'

print(calcular_custo(500))  # Exemplo com argumento posicional quantidade e calculo com valor padrão
print(calcular_custo(420, 12.0)) # Exemplo apenas argumentos posicionais
print(calcular_custo(quantidade=300, custo_unitario=6.75))
print(calcular_custo(custo_unitario=6.75, quantidade=300))


