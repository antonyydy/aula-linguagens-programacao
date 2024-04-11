entrada = str(input())
entrada = entrada.split()
a = int(entrada[0])
b = int(entrada[1])

if (a % b == 0 or b % a == 0):
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")

