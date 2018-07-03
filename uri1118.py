soma = 0
i = 0
controle = True
while True:
    if controle == False:
        print("novo calculo (1-sim 2-nao)")
        sn = input()
        if sn == 1:
            controle = True
        if sn == 2:
            break
    if controle == True:
        nota = float(input())
        if nota < 0 or nota > 10:
            print("nota invalida")
        else:
            soma = soma + nota
            i = i + 1
        if i == 2:
            media = soma/2
            print("media = %.2f" %media)
            i = 0
            soma = 0
            controle = False
