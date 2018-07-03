#duas funções uma para encripitar e outra para desencriptar strings.


def encripta(texto):
    crip = ''
    for b in range(len(texto)):
        if ord(texto[b])<65 or (ord(texto[b]) > 90 and ord(texto[b]) < 97) or ord(texto[b])>122:
            crip = crip + texto[b]
        else:
            crip= crip + chr(ord(texto[b])+3)
    crip2 = crip[::-1]
    metade = len(crip2)/2
    crip3 = crip2[:metade]
    crip2 = crip2[metade:]
    for b in range(len(crip2)):
        crip3 = crip3 + chr(ord(crip2[b])-1)
    print(crip3)


    
def desencripta(x):
    metade = len(x)/2
    crip1 = x[:metade]
    crip2 = x[metade:]
    for b in range(len(crip2)):
        crip1 = crip1 + chr(ord(crip2[b])+1)
    texto = crip1[::-1]
    crip = ''
    for b in range(len(texto)):
            if ord(texto[b])-3<65 or (ord(texto[b])-3 > 90 and ord(texto[b])-3 < 97) or ord(texto[b])-3>122:
                crip = crip + texto[b]
            else:
                crip= crip + chr(ord(texto[b])-3)
    return crip
    
    
    
    
