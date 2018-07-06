while True:
    try:
        palavra = raw_input()
        resp = ''
        i = 0
        for b in palavra:
            if b == ' ':
                resp = resp + b
            else:
                if b != ' ' and i%2==0:
                    resp = resp + b.upper()
                else:
                    resp = resp + b.lower()
                i =  i + 1
        print(resp)
                
    except EOFError:
        break
