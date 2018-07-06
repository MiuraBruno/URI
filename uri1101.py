while True:
    x = raw_input().split()
    a1 = int(x[0])
    a2 = int(x[1])
    if a1 <= 0 or a2 <= 0:
        break
    else:
        if a1>a2:
            a1,a2 = a2,a1
        v = str(range(a1,a2+1)).replace("[","").replace("]","").replace(",","")
        soma = (-(a1*a1) + (a2*a2) + a1 + a2)/2
        print("%s Sum=%d" %(v,soma))
        
