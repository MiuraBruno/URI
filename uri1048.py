salario = float(input())
aumento = {400:15.0,800:12.0,1200:10.0,2000:7.0}
novo = 0
for b in aumento:
    if salario <= b:
        percent = aumento[b]
        novo = salario*(1.0+(percent/100))
        reajuste = novo - salario
        break
        
if novo == 0:
    percent = 4.0
    novo = salario *(1.0+(percent/100))
    reajuste = novo - salario
percent = str(int(percent)) + " %"  
print("Novo salario: %.2f" %novo)
print("Reajuste ganho: %.2f" %reajuste)
print("Em percentual: %s" %percent)
