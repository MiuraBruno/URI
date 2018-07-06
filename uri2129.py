def factorial(n):
    if n < len(_FAC_TABLE):
        return _FAC_TABLE[n]

    last = len(_FAC_TABLE) - 1
    total = _FAC_TABLE[last]
    for i in range(last + 1, n + 1):
        total *= i
        _FAC_TABLE.append(total)

    return total
i = 1
while True:
    try:
        n = input()
        x = str(factorial(n)).replace("0","")
        print("Instancia %d" %i)
        print("%s\n" %x[-1])
        
        i = i + 1
        
    except EOFError:
        break
