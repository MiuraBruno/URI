a = int(input())
for b in range(a):
    n = int(input())
    def primo(n):
        from math import *
        if n % 2 == 0: return n == 2
        divisor = 3
        raiz = floor(sqrt(n))
        while divisor <= raiz and n % divisor != 0:
            divisor += 2
        return n > 1 and divisor > raiz
    if primo(n) == True:
        print("Prime")
    else:
        print("Not Prime")
