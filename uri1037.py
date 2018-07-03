#verificar se um dado número está contido entre intervalos determinados ou
#se estão fora desses intervalos
entrada = float(input())
inter = {25:"[0,25]",50:"(25,50]",75:"(50,75]",100:"(75,100]"}
if entrada < 0 or entrada > 100:
    print("Fora de intervalo")
else:
    for b in inter:
        if entrada<=b:
            print("Intervalo %s" %inter[b])
            break

            
