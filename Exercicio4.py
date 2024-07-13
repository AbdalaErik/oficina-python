'''
OFICINA DE PYTHON - Lista de Exercícios - Exercício 4

Aluno: Erik Bolonha Abdala

Escreva um programa que armazene as disciplinas de um curso (por exemplo,
Matemática, Física, Química, História e Letras) em uma lista, pergunte ao
usuário a nota que ele recebeu em cada disciplina e elimine da lista as
disciplinas aprovadas. Ao final, o programa deverá exibir na tela os
assuntos que o usuário deverá repetir.
'''

print("# Exercício 4 - Análise de disciplinas\n")

# Lista de disciplinas:

disciplinas = ["Matemática", "Física", "Química", "História", "Geografia"]

#Critério para aprovação: nota >= 6

print("- Disciplinas a serem analisadas:", disciplinas, "\n")

for disciplina in disciplinas.copy():
    
    nota = float(input("> Informe a nota para a disciplina " + disciplina + ": "))
    
    if nota >= 6:
        
        disciplinas.remove(disciplina)
    
print("\n- Disciplinas pendentes:", disciplinas)
