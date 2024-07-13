'''
OFICINA DE PYTHON - Lista de Exercícios - Exercício 6

Aluno: Erik Bolonha Abdala

Escreva um programa que armazene os números de 1 a 20 em uma lista
e os exiba na tela na ordem inversa, separados por vírgulas.
'''

print("# Exercício 6 - Ordem inversa dos números de uma lista\n")

lista = list(range(1, 21))
    
print("- Lista:", lista, "\n")
    
lista.reverse()

resultado = ', '.join(str(x) for x in lista)

print("- Resultado:", resultado)
