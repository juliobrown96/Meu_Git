def is_fibonacci(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b == n

num = int(input("Informe um número: "))
print(f"{num} pertence à sequência." if is_fibonacci(num) or num == 0 else f"{num} NÃO pertence à sequência.")