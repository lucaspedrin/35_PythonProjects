num = int(input('Digite um número: '))

unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10

print(f'Unidade: {unidade}\nDezena: {dezena}\nCentena: {centena}\nMilhar: {milhar}')