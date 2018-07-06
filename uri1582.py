def mdc(a, b):
    while a % b != 0:
        a, b = b, a % b
    return b 
while True:
    try:
        n = raw_input().split()
        v = []
        for b in n:
            v.append(int(b))
        v = sorted(v)    
        if (v[2])**2 == (v[0])**2 + (v[1])**2:
            if mdc(mdc(v[0],v[1]),v[2]) == 1:
                print("tripla pitagorica primitiva")
            else:
                print("tripla pitagorica")
        else:
            print("tripla")

            
    except EOFError:
        break
