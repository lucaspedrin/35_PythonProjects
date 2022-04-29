frase = str(input('Digite algo: ')).lower().strip()

quantidade = frase.count('a')
primeiro_a = frase.find('a') + 1
ultimo_a = frase.rfind('a') + 1

print(f'\033[32mA quantidade de "a" é de: {quantidade}')
print(f'\033[34mO primeiro "a" aparece na posição: {primeiro_a}')
print(f'\033[35mO último "a" aparece na posição: {ultimo_a}')