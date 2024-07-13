'''
OFICINA DE PYTHON - Lista de Exercícios - Exercício 1

Aluno: Erik Bolonha Abdala

Realize o exercício referente à Calculadora de Índice de Massa Corporal (IMC)
conforme descrito durante a oficina de Python. O enunciado pertinente está
disponível no PDF da apresentação. (Exercício no slide 16 da apresentação).
'''

print("# Exercício 1 - Calculadora de Índice de Massa Corporal (IMC)\n")

altura = float(input("> Informe sua altura: "))

peso = float(input("> Informe seu peso: "))

imc = peso / pow(altura, 2)

imc_formatado = round(imc, 1)

if(imc_formatado < 18.5):
    
    print("\n- Seu IMC é", imc_formatado, "e você está abaixo do peso.")

elif (imc_formatado >= 18.5) and (imc_formatado <= 24.9):
    
    print("\n- Seu IMC é", imc_formatado, "e você está com peso normal.")

elif (imc_formatado > 24.9):
    
    print("\n- Seu IMC é", imc_formatado, "e você está com sobrepeso.")
