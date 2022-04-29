n1 = int(input('Digite o primeiro valor inteiro: '))
n2 = int(input('Digite o segundo valor inteiro: '))
n3 = int(input('Digite o terceiro valor inteiro: '))

menor = n1
maior = n1

if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print(f'\033[32mO menor número digitado foi: {menor}\033[m')
print(f'\033[34mO maior número digitado foi: {maior}\033[m')