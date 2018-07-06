n = input()
for b in range(n):
    num = raw_input().split()
    v1 = str(range(int(num[0]),int(num[1])+1)).replace("[","").replace("]","").replace(",","").replace(" ","")
    resp = v1 + v1[::-1]
    print(resp)
