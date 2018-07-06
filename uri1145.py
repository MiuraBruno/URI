a = 1
n = raw_input().split()
inicio = int(n[0])
fim = int(n[1])
while a<=fim:
    v = str(range(a,inicio+1)).replace("[","").replace("]","").replace(",","")
    inicio = inicio + int(n[0])
    a = a + int(n[0])
    print("%s" %(v))

    
