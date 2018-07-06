nomes = {0:"Rafael",1:"Beto",2:"Carlos"}
n = input()
for b in range(n):
    xy = raw_input().split()
    v = []
    for i in xy:
        v.append(float(i))
    resultados = []
    resultados.append((3*v[0])**2 + (v[1])**2)
    resultados.append(2*((v[0])**2) + (5*v[1])**2)
    resultados.append(-100*v[0] + v[1]**3)
    bla = resultados.index(max(resultados))
    print("%s ganhou" %nomes[bla])
