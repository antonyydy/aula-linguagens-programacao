entrada = str(input())
entrada = entrada.split()
a = int(entrada[0])
b = int(entrada[1])
c = int(entrada[2])

MaiorAB = (a + b + abs(a - b)) / 2
(maior_valor) = (MaiorAB + c + abs(MaiorAB - c)) / 2

print(f"{int(maior_valor)} eh o maior")