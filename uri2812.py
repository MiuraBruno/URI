def remove_pares(lista, tamanho_lista):
    lista_impares = []
    for i in range(tamanho_lista):
        if int(lista[i]) %2 != 0:
            lista_impares.append(int(lista[i]))
    return lista_impares
        
num_casos = input()
for i in range(num_casos):
    tamanho_lista = input()
    lista = raw_input().split()
    lista = remove_pares(lista, tamanho_lista)
    lista = sorted(lista)
    s = ""
    a=0
    count_maior = len(lista)-1
    count_menor = 0
    while(count_menor != count_maior+1
          ):
        if a == 0:
            s += str(lista[count_maior]) + " "
            a=1
            count_maior -= 1
        else:
            s += str(lista[count_menor]) + " "
            a=0
            count_menor += 1
    print(s[:-1])
