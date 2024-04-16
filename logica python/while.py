# uso do while

notas = []
nota = float(input())

while nota != -1:
    notas.append(nota)
    nota = float(input())



soma = sum(notas)
media = soma / len(notas)
print(media)