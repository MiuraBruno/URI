#table é uma tabela de preço dos produtos
#recebe o código do produto e a quantidade de itens que foram comprados
v = raw_input().split()
table = {1:4.00,2:4.5,3:5.0,4:2.0,5:1.5}
result = table[int(v[0])]*int(v[1])
print("Total: R$ %.2f" %result)
