#calculo da média do aluno com peso nas notas.
#restrições para aprovação reprovado e exame onde se calcula uma nova média
notas = raw_input().split()
media = 2*float(notas[0]) + 3*float(notas[1]) + 4*float(notas[2]) + 1*float(notas[3])
media = media/10
print("Media: %.1f" %(media))
if media>= 7:
    print("Aluno aprovado.")
else:
    if media<5:
        print("Aluno reprovado.")
    else:
        print("Aluno em exame.")
        exame = float(input())
        print("Nota do exame: %.1f" %(exame))
        media2 = (media+exame)/2
        if media>= 5:
            print("Aluno aprovado.")
        else:
            print("Aluno reprovado.")
        print("Media final: %.1f" %(media2))
            
