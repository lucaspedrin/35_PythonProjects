cidade = str(input('Qual a sua cidade? ')).strip().split()
santo = 'santo' in cidade[0].lower()
print(f'Seu nome começa com santo? {santo}')