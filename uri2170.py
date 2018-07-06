i = 1
while True:
    try:
        if i != 1:
            print("")
        val = raw_input().split()
        x = float(val[0])
        y = float(val[1])
        z = y - x
        b = z*100/x            
        print("Projeto %d:" %i)
        print("Percentual dos juros da aplicacao: %.2f %s" %(b,chr(37)))
        i = i + 1
    except EOFError:
        break
