print (" Vamos dar as medias de notas do alunos")

nota1 = float (input("digite a nota 1: "))
nota2 = float (input("digite a nota 2: "))
nota3 = float (input("digite a nota 3: "))
nota4 = float (input("digite a nota 4: "))
media = (nota1 + nota2 + nota3 + nota4)/4
print (" A media do aluno é:", f"{media:2.2f}")

if media >=7:
    print (" o aluno foi aprovado ")
if media <4:
    print ("o aluno foi reprovado ");
if media >=4 and media <7:
    print ("o aluno está de recuperação ")
print ("o aluno ficou de recuperação, mas ainda tem chance de passar. agora o aluno vai receber uma prova de recuperação, ")

nota5 = float (input("digite a nota da prova de recuperação: "))
media_da_recuperação = (media + nota5)/2

if float(media_da_recuperação) >=7:
    print ("o aluno foi aprovado no ano letivo com a nota da recuperação. a media final do aluno é ", f"{media_da_recuperação:2.2f}")
if float(media_da_recuperação) <=4:
    print ("o aluno foi reprovado no ano letivo mesmo com a nota da recuperação . a media final do aluno é ", f"{media_da_recuperação:2.2f}")
