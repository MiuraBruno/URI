while True:
    tempo = float(input())
    tempob = tempo
    tempoa = tempo
    alemanha = 0
    brasil = 0
    if tempo == 0:
        break
    else:
        brasil = tempob/90
        alemanha = tempo/(90.0/7.0)
        if alemanha > int(alemanha):
            alemanha = alemanha + 1
            alemanha = int(alemanha)
        print("Brasil %d x Alemanha %d" %(brasil,alemanha))
