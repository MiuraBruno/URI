while True:
    a = type(1)
    n = input()
    print(type(n))
    if str(n)[0]=='-':
        break
    if len(str(n))>1:
        if a!=type(n):
            print"hue"
            resposta = str(n)
        else:
            resposta = hex(int(n))
    else:
        resposta = hex(int(n))
    if resposta[-1] == "L":
        resposta = resposta[:-1]
    print(resposta)
