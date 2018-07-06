n = input()
v = []
for b in range(n):
    pais = raw_input().split()
    aux = []
    i = 1
    while i <= 3:
        a = int(pais[i])
        aux.append(a)
        i = i + 1
        
    v.append((aux,pais))
resp = sorted(v,reverse=True)
for b in resp:
    print(str(b[-1]).replace("[","").replace("]","").replace(",","").replace("'",""))
