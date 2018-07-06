a1 = input()
a2 = input()

if a1>a2:
    a1,a2 =  a2,a1
while a1<(a2-1):
    a1 = a1 + 1
    if a1%5 == 2 or a1%5 == 3:
        print(a1)
