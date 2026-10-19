def taxa_com_print(produzidas, rejeitadas):
    print(round(rejeitadas / produzidas * 100, 2))

def taxa_com_return(produzidas, rejeitadas):
    return round(rejeitadas / produzidas * 100, 2)

a = taxa_com_print(500, 12)
b = taxa_com_return(500, 12)
print("a =", a)
print("b =", b)
print("Diferença para a meta de 3%:", 3.0 - b)

print("Diferença para a meta de 3%:", 3.0 - a)



# Ocorre a excessão pois a função taxa_com_print não retorna nenhum valor. 
# Retornando  o erro TypeError pois no print tenta realizar um calculo entre 
# um tipo float e o tipo None.