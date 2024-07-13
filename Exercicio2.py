'''
OFICINA DE PYTHON - Lista de Exercícios - Exercício 2

Aluno: Erik Bolonha Abdala

Escreva um laço que calcule a soma de todos os números pares entre 2 e 100.
'''

print("# Exercício 2 - Soma de todos os números pares entre 2 e 100\n")

soma = 0

for num in range(2, 101, 2):
    
    soma += num

print(f"- A soma dos números pares entre 2 e 100 é: {soma}")
