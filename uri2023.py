v = []
i = 0
while True:
    try:
        nome = raw_input()
        if i == 0:
            v.append(nome)
            i = i + 1
        else:
            if v[0].upper()<nome.upper():
                v[0] = nome
        
        
    except EOFError:
        print(v[0])
        break
