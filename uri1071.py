a = input()
b = input()
if a>b:
    a,b=b,a
i = 0
if a%2==0:
    a = a + 1
else:
    a = a + 2
if b%2==0:
    b = b-1
else:
    b = b -2
n = ((a+b)*(b-a+2))/4
print(n)
