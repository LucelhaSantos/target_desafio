def is_fibonacci(num):
    a, b = 0, 1
    while b <= num:
        if b == num:
            return f"{num} pertence à sequência de Fibonacci."
        a, b = b, a + b
    return f"{num} não pertence à sequência de Fibonacci."

# Exemplo de uso
numero = 21  # Pode ser trocado por outro número ou definido como input
print(is_fibonacci(numero))
