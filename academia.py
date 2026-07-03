from abc import ABC, abstractmethod
from time import sleep
from rich import print
from rich.panel import Panel
class Treino(ABC):
    def __init__(self, nome, duracao):
        self.nome = nome
        self.duracao = duracao
        
    def __str__(self):
        return f"{self.nome} - {self.duracao} minutos"
        
        
    @abstractmethod
    def executar(self):
        pass
    
    @abstractmethod
    def calcular_calorias(self):
        pass
    

class Musculacao(Treino):
    def calcular_calorias(self):
        return self.duracao * 4.6
    def executar(self):
        print(f"Iniciando o treino de {self.nome} por {self.duracao} minutos!")
        sleep(1.5)
        print(f"Treino de musculação finalizado.")
        print(f"Calorias gastas: {self.calcular_calorias():.1f}\n")
        

class Cardio(Treino):
    def calcular_calorias(self):
        return self.duracao * 2.1
    def executar(self):
        print(f"Iniciando o treino de {self.nome} por {self.duracao} minutos!")
        sleep(0.8)
        print(f"Cardio finalizado.")
        print(f"Calorias gastas: {self.calcular_calorias():.1f}")
        
class Alongamento(Treino):
    def calcular_calorias(self):
        return self.duracao * 1.6
    def executar(self):
        print(f"Iniciando o treino de {self.nome} por {self.duracao} minutos!")
        sleep(1)
        print(f"Alongamento finalizado.")
        print(f"Calorias gastas: {self.calcular_calorias():.1f}")
        
        
class Aluno:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.treinos = []
        
        
    def adicionar_treino(self, treino):
        self.treinos.append(treino)
        
    def mostrar_treinos(self):
        if not self.treinos:
            print("Nenhum treino cadastrado!")
            return
        
        for i, treino in enumerate(self.treinos, start=1):
             print(f"{i} - {treino}")
            
    def treinar(self):
        if not self.treinos:
            print("Nenhum treino cadastrado!")
            return
    
        for treino in self.treinos:
            treino.executar()
    
    def calorias_totais(self):
        total = 0

        for treino in self.treinos:
            total += treino.calcular_calorias()

        print(f"Calorias totais: {total:.0f} kcal")

aluno = Aluno("Luis", 17)
def menu(aluno):
    conteudo = f"""
Nome: {aluno.nome}
Idade : {aluno.idade}
    
    
1 - Adicionar treino
2 - Mostrar treinos
3 - Iniciar treino
4 - Sair"""

    painel = Panel(conteudo, width=40, title="SISTEMA DE ACADEMIA")
   

    while True:
        print(painel)
    
        op = input("Escolha uma opção: ")
        if op == "1":
            treinos = f"""Escolha o tipo de treino:
1 - Musculacao
2 - Cardio
3 - Alongamento"""
            painel_de_treinos = Panel(treinos, width=40, title="TREINOS")
            print(painel_de_treinos)
            escolha = str(input("Opção: "))
            nome = input("Qual treino iremos fazer hoje? ")
            duracao = int(input("Em minutos, qual será a duração do treino: "))
            
            treino = None

            if escolha == "1":
                treino = Musculacao(nome, duracao)

            elif escolha == "2":
                treino = Cardio(nome, duracao)

            elif escolha == "3":
                treino = Alongamento(nome, duracao)

            else:
                print("Opção inválida.")

            if treino:
                aluno.adicionar_treino(treino)
                print("\nTreino adicionado com sucesso!")
        
        elif op == "2":
            aluno.mostrar_treinos()
        
        elif op == "3":
                aluno.treinar()
                aluno.calorias_totais()
            
        elif op == "4":
            print("\nSaindo...")
            break

        
        

menu(aluno)
