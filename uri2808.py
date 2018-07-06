dic_position = {"a":"1","b":"2","c":"3","d":"4","e":"5","f":"6","g":"7","h":"8"}
position = raw_input().split()
inicio = position[0]
inicio = dic_position[inicio[0]] + inicio[1]
fim = position[1]
fim = dic_position[fim[0]] + fim[1]
v_validos = []
print(type(inicio))
print(type(fim))

