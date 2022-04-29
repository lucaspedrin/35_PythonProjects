nome = str(input('Qual é o seu nome completo? ')).strip()

maiúsculas = nome.upper()
minúsculas = nome.lower()
sem_espaço = len(''.join(nome.split()))
primeiro_nome = nome.split()[0]

print(f'Seu nome em maiúsculas é: {maiúsculas}\nSeu nome em minúsculas é: {minúsculas}')
print(f'Seu nome completo tem {sem_espaço} letras.\nSeu primeiro nome é {primeiro_nome} e ele tem {len(primeiro_nome)} letras.')