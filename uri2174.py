n = input()
v = []
for b in range(n):
    a = raw_input()
    v.append(a)
x = 151 - len(list(set(v)))
print("Falta(m) %d pomekon(s)." %x)
    
