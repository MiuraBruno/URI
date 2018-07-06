n = input()
ind = raw_input().split()
indices = [] 
for b in ind:
    indices.append(int(b)-1)
v = range(n)
v2 = v
aux = []
indices2 = indices
for b in indices:
    a = v[b]
    print(a)
    resposta = v2.index(a)
    v2.remove(resposta)
    aux.append(resposta)
print(resposta)
