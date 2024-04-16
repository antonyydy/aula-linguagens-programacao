

#substituir letras
n = input("seu nome: ")
i = int(input("posição que deseja adicionar a letra: "))
print(n[i])

if n[i] == "s":
    print(n[:i]+"r"+n[i+1:])
elif n[i] == "m" : 
    print(n[:i]+"n"+n[i+1:])
else:
    print(n[:i]+n[i+1:])