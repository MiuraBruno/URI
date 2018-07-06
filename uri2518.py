import math
while True:
    try:
        n = input()
        lados = raw_input().split()
        v = []
        for b in lados:
            v.append(float(b))
        h = v[0]*n
        c = v[1]*n
        x = math.hypot(h,c)
        base = x*v[2]/10000.0
        print("%.4f" %base)
    except EOFError:
        break
