n = input()
for i in range(n):
    palavra = raw_input()
    if len(palavra) == 5:
        print("3")
    elif (palavra[1] == "n" and palavra[2] == "e"):
        print("1")
    elif (palavra[0] == "o" and palavra[2] == "e"):
        print("1")
    elif (palavra[0] == "o" and palavra[1] == "n"):
        print("1")
    else:
        print("2")
