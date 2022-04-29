print('\033[1;33m' + '-=-' * 9)
print(' Verificador de triângulos')
print('-=-' * 9 + '\033[34m')

a = float(input('Digite o primeiro segmento: '))
b = float(input('Digite o segundo segmento: '))
c = float(input('Digite o terceiro segmento: '))

if a < b + c and b < a + c and c < a + b:
    print('\033[1;32m' + 'É possível formar um triângulo!')
else:
    print('\033[1;31m' + 'Não é possível formar um triângulo!')