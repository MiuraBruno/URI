cont = raw_input()
cont = cont.replace("7","0").split()
if cont[1] == "+":
    resp = str(int(cont[0]) + int(cont[2])).replace("7","0")
else:
    resp = str(int(cont[0])*int(cont[2])).replace("7","0")
print(int(resp))
    

