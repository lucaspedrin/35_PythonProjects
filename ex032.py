from datetime import date

ano = int(input('Digite um ano qualquer (0 para usar o ano atual): '))

if ano == 0: 
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'\033[32mO ano de {ano} é um ano BISSEXTO!')
else:
    print(f'\033[31mO ano de {ano} NÃO é um ano BISSEXTO!')