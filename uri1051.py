valor = {3000.00:0.08,4500.00:0.18,4500.01:0.28}
a = float(input())
resultado = 0
if a<=2000.00:
    print("Isento")
else:
    while a > 0:
        a = a - 2000.00
        for b in valor:
            if a<=valor[b]:
                break
            else:
                break
        resultado = a * valor[b]
    print("R$ %.2f" %(resultado))
    
