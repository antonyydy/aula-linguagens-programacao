
while True:
    try:
        A = int(input())
        B = int(input())
        C = int(input())
        D = int(input())
        break
    except ValueError:
        print("Algumas entradas são inválidas. Por favor, digite apenas números inteiros.")

DIFERENCA = (A * B - C * D)

print("DIFERENCA = ", DIFERENCA)

