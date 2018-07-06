empate = 0
inter = 0
gremio = 0
i = 0
while True:
    n = raw_input().split()
    i = i + 1
    goli =  int(n[0])
    golg = int(n[1])
    if goli == golg:
        empate == empate + 1
    elif goli > golg:
        inter = inter + 1
    else:
        gremio = gremio + 1
    print("Novo grenal (1-sim 2-nao)")
    zerar = input()
    if zerar == 2:
        print("%d grenais" %i)
        print("Inter:%d" %inter)
        print("Gremio:%d" %gremio)
        print("Empates:%d" %empate)
        if inter == gremio: 
            print("Nao houve vencedor")
        elif inter> gremio:
            print("Inter venceu mais")
        else:
            print("Gremio venceu mais")
        break
