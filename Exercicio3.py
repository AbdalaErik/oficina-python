'''
OFICINA DE PYTHON - Lista de Exercícios - Exercício 3

Aluno: Erik Bolonha Abdala

Com base nos estudos de Programação Orientada a Objetos (POO), solicita-se o
desenvolvimento de três classes à escolha, com a atribuição de pelo menos três
atributos em cada uma delas. Posteriormente, é necessário concatená-las e
inserir os dados conforme exemplificado durante a oficina de Python. Por fim,
o programa deve apresentar os resultados ao usuário ao ser executado.
'''

print("# Exercício 3 - Programação Orientada a Objetos (POO)\n")

class Item:
    
    def __init__(self, nome, tipo, efeito):
        
        self.nome = nome
        self.tipo = tipo
        self.efeito = efeito

    def exibir_item(self):
        
        print(f"- INFORMAÇÕES DO ITEM\n"
              f"  [Nome]: {self.nome}\n"
              f"  [Tipo]: {self.tipo}\n"
              f"  [Efeito]: {self.efeito}\n")
        
class Personagem:
    
    def __init__(self, nome, classe, nivel, item=None):
        
        self.nome = nome
        self.classe = classe
        self.nivel = nivel
        self.item = item

    def exibir_personagem(self):
        
        print(f"- INFORMAÇÕES DO PERSONAGEM\n"
              f"  [Nome]: {self.nome}\n"
              f"  [Classe]: {self.classe}\n"
              f"  [Nível]: {self.nivel}\n")
                
        if self.item is not None:
            self.item.exibir_item()
        else:
            print("- O personagem ainda não possui nenhum item.\n")

class Jogador:
    
    def __init__(self, nome, idade, plataforma, 
                 tempo_de_jogo, personagem=None):
        
        self.nome = nome
        self.idade = idade
        self.plataforma = plataforma
        self.tempo_de_jogo = tempo_de_jogo
        self.personagem = personagem

    def exibir_tudo(self):
        
        print(f"- INFORMAÇÕES DO JOGADOR\n"
              f"  [Nome]: {self.nome}\n"
              f"  [Idade]: {self.idade}\n"
              f"  [Plataforma]: {self.plataforma}\n"
              f"  [Tempo de jogo]: {self.tempo_de_jogo} hora(s)\n")
              
        if self.personagem is not None:
            self.personagem.exibir_personagem()
        else:
            print("- O jogador ainda não possui nenhum personagem.\n")
            
print("===================== Jogador 1 =====================\n")

item1 = Item("Poção de Cura", "Consumível", "Recupera 25% de vida.")
personagem1 = Personagem("Guts", "Berserker", 46, item1)
jogador1 = Jogador("Erik", 25, "PC", 350, personagem1)

jogador1.exibir_tudo()

print("===================== Jogador 2 =====================\n")

personagem2 = Personagem("Dante", "Swordmaster", 32)
jogador2 = Jogador("Luiz", 18, "PS5", 45, personagem2)

jogador2.exibir_tudo()

print("===================== Jogador 3 =====================\n")

jogador3 = Jogador("João", 40, "PC", 0)

jogador3.exibir_tudo()
