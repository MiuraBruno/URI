n = input()
for b in range(n):
    x = raw_input().split()
    a1 = int(x[0])
    a2 = int(x[1])
    if a1 == a2:
        print(0)
    else:
        if a1>a2:
            a1,a2=a2,a1
        i = 0
        if a1%2==0:
            a1 = a1 + 1
        else:
            a1 = a1 + 2
        if a2%2==0:
            a2 = a2-1
        else:
            a2 = a2 -2
        n = ((a1+a2)*(a2-a1+2))/4
        print(n)
