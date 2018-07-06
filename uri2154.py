while True:
    try:
        n = input()
        if n !=1:
            func = raw_input().replace(" ","").split("+")
            resp = ''
            for b in range(len(func)):
                aux = func[b].split("x")
                coefa = int(aux[0]) * int(aux[-1])
                exp = int(aux[-1]) - 1
                resp = resp + str(coefa) + "x" + str(exp) + ' + '
            resp = resp[:-3]
            if resp[-1] == '1':
                resp = resp[:-1]
            print(resp)
        else:
            func = raw_input()
            coefa = int(func[0]) * int(func[2])
            exp = int(func[2]) - 1
            print("%dx%d"%(coefa,exp))
    
    except EOFError:
        break
    
