'''
OFICINA DE PYTHON - Lista de Exercícios - Exercício 5

Aluno: Erik Bolonha Abdala

Escreva um programa que armazene o alfabeto em uma lista, elimine da
lista as letras que ocupam posições múltiplas de 3 e exiba a lista
resultante na tela.
'''

print("# Exercício 5 - Posições múltiplas de 3 no alfabeto\n")

# Alfabeto:

alfabeto = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 
    'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 
    'U', 'V', 'W', 'X', 'Y', 'Z'
]

print("- Alfabeto:", alfabeto)

posicoes_filtradas = []

for indice, letra in enumerate(alfabeto.copy()):
    
    if (indice % 3) == 0:
        
        alfabeto.remove(letra)
        
        posicoes_filtradas.append([indice, letra])
    
print("\n- Posições filtradas:", posicoes_filtradas)

print("\n- Alfabeto filtrado:", alfabeto)
