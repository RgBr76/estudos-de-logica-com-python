# Definindo uma lista de números
numeros = [10, 20, 30, 40, 50]

# Inicializando uma variável para armazenar a soma dos números
soma = 0

# Iterando sobre a lista de números
for numero in numeros:
    # Adicionando o número atual à soma
    soma += numero

# Calculando a média dos números
media = soma / len(numeros)

# Exibindo a soma e a média
print(f"A soma dos números é: {soma}")
print(f"A média dos números é: {media}")