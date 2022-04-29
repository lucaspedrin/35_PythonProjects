from random import randrange

print('-=-' * 12)
print(f'Tente adivinhar um número de 0 a 5!')
print('-=-' * 12)

sorteado = randrange(0, 5)
sugestão = int(input('Digite um número de 0 a 5: '))

if sugestão >= 0 and sugestão <= 5:
    if sorteado == sugestão:
        print('\033[32mParabéns! Você ACERTOU!')
        print(f'O número sugerido foi {sugestão} e o número sorteado foi {sorteado}')
    else:
        print('\033[31mQue pena! Você ERROU!')
        print(f'O número sugerido foi {sugestão} e o número sorteado foi {sorteado}')
else:
    print('\033[1;31mPor favor, digite um número entre 0 e 5!')