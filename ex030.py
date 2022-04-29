num = int(input('Digite um número: '))

if num % 2 == 0:
    print(f'\033[1;34mO número {num} é PAR!')
else:
    print(f'\033[1;31mO número {num} é ÍMPAR!')