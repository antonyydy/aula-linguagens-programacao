# funções len, upper, lower e posições

# nome = input()
# sobrenome = input()
# size = len(nome)

# print(nome[0].lower() + nome[1:].upper())
# print(sobrenome[0].upper() + sobrenome[1:].lower())

nome = str(input())
sobrenome = str(input())
data = int(input())

nome_Menor = nome.lower()
sobrenome_Maior = sobrenome.upper()

print(f"{nome_Menor} {sobrenome_Maior} nasceu no ano de {data}")