while True:
    num = raw_input().split()
    n = int(num[0])
    m = int(num[1])
    if n == 0 and m == 0:
        break
    else:
        soma = str(n+m).replace("0","")
        print(soma)
