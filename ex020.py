from random import shuffle

aluno1 = str(input('O nome do primeiro aluno: '))
aluno2 = str(input('O nome do segundo aluno: '))
aluno3 = str(input('O nome do terceiro aluno: '))
aluno4 = str(input('O nome do quarto aluno: '))

ordem = [aluno1, aluno2, aluno3, aluno4]

shuffle(ordem)

print(f'A ordem de apresentação será:\n{ordem}')