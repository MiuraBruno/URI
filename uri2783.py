leia = raw_input().split()
carimbadas = raw_input().split()
compradas = raw_input().split()
compradas = list(set(compradas))
faltantes = len(list(set(carimbadas)-set(compradas)))
print(faltantes)