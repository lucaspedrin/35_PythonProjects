nome = str(input('Qual é o seu nome completo? ')).strip().split()

primeiro_nome = nome[0]
ultimo_nome = nome[len(nome) - 1]

print(f'Seu primeiro nome é \033[4;35m{primeiro_nome}\033[m e seu último nome é \033[4;35m{ultimo_nome}')