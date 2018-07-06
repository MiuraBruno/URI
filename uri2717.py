n = input()
pre = raw_input().split()
v = []
for b in pre:
    v.append(int(b))
tempo = sum(v)
if tempo>n:
    print("Deixa para amanha!")
else:
    print("Farei hoje!")
