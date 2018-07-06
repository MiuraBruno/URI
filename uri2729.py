n = input()
for b in range(n):
    compra = raw_input().split()
    compra = list(set(compra))
    compra = sorted(compra)
    resp = ''
    for i in range(len(compra)-1):
        resp = resp + compra[i] + ' '
    resp = resp + compra[-1]
        
    print(resp)
