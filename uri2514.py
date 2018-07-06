def gcd(x, y):
   while(y):
       x, y = y, x % y

   return x
def lcm(x, y):
   lcm = (x*y)//gcd(x,y)
   return lcm
while True:
    try:
        ano = input()
        luas = raw_input().split()
        v =[]
        for b in luas:
            v.append(int(b))
        print(lcm(lcm(v[0],v[1]),v[2])-ano)
    except EOFError:
        break
