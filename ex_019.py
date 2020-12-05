"""
#Método 1 de sortear uma lista

import random

aluno1 = str(input("Aluno 1: "))
aluno2 = str(input("Aluno 2: "))
aluno3 = str(input("Aluno 3: "))
aluno4 = str(input("Aluno 4: "))
lista_de_aluno = [aluno1, aluno2, aluno3, aluno4]
print(f'o aluno escolhido foi {lista_de_aluno[random.randrange(0,3)]}')

"""

#Método 2 de sortear uma lista

import random

aluno1 = str(input("Aluno 1: "))
aluno2 = str(input("Aluno 2: "))
aluno3 = str(input("Aluno 3: "))
aluno4 = str(input("Aluno 4: "))
lista_de_alunos = [aluno1, aluno2, aluno3, aluno4]
escolhido = random.choice(lista_de_alunos)
print(f'o aluno escolhido foi {escolhido}')
