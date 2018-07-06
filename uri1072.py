a = input()
dentro = 0
fora = 0
for b in range(a):
    n = input()
    if n>=10 and n<=20:
        dentro = dentro + 1
    else:
        fora = fora + 1

print("%d in" %dentro)
print("%d out" %fora)
