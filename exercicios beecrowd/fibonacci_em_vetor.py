T = int(input())

for i in range(T):
    N = int(input())
    
    if N == 0:
        result = 0
    elif N == 1:
        result = 1
    else:
        a, b = 0, 1
        for i in range(2, N + 1):
            a, b = b, a + b
        result = b
    
    print(f"Fib({N}) = {result}")
