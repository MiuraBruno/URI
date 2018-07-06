a = input()
for b in range(a):
    numero = raw_input().split()
    qtd = float(numero[0])
    numeros = []
    for b in numero:
        numeros.append(float(b))        
    numeros = numeros[1:]
    media = sum(numeros)/qtd
    acima = 0
    for b in numeros:
        if b > media:
            acima = acima + 1
    acima = 100*acima/qtd
    imprimi = "%"
    print("%.3f%s" %(acima,imprimi))
