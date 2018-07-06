#inseri 4 valors e faz uma comparação para verificar se estão aceitos ou não
v = raw_input().split()
a,b,c,d = int(v[0]),int(v[1]),int(v[2]),int(v[3])
if b>c and d>a and c+d > a+b and c>=0 and d >=0 and a %2 ==0:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")
