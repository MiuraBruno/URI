result = {'0 0 0':'*','0 0 1':'C', '0 1 0':"B", '0 1 1':"A",'1 0 0':"A",'1 0 1':"B",'1 1 0':"C", '1 1 1':"*"}
while True:
    try:
        jogo = raw_input()
        print("%s" %(result[jogo]))
    except EOFError:
        break
