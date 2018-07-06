while True:
    n = input()
    if n == 0:
        break
    else:
        v = str(range(1,n+1)).replace("[","").replace("]","").replace(",","")
        print("%s" %(v))
