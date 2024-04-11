# uso do for e append

lista_nota = []
acm = 0

for i in range(0, 10):
    lista_nota = float(input('nota['+str(i)+']:'))
    lista_nota.append(lista_nota)

    
    
acm = acm + lista_nota
r = i + 1
media = acm/r



if media >= 7:
    print(f"SUA MEDIA FOI BOA: {media} APROVADO!!!!!!!!!!!!!!!!")
else: 
    print(f"SUA MEDIA FOI UM LIXO: {media} REPROVADO!!!!!!!!!!!!!!!!!")