# O código abaixo é uma tentativa de criar um verificador de palíndromos.
# Palíndromos são palavras ou frases que são iguais quando lidas de trás para frente.
# No entanto, o código está incompleto e contém erros.
# Complete e corrija o código para que ele funcione corretamente.
# O usuário deve digitar uma palavra ou frase, e o programa deve imprimir se é um palíndromo ou não.
# Ignore espaços, pontuações e diferenças entre maiúsculas e minúsculas.

texto = input("Digite um texto: ")
texto = texto.lower()
delimitador = ''
sem_espaco = delimitador.join(texto)

texto_invertido = sem_espaco[::-1]  # Esta linha pode precisar de ajustes
print(texto_invertido)
print(sem_espaco)
if sem_espaco == texto_invertido:
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")