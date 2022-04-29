distancia = float(input('Qual a distância da viagem (Km)? '))

if distancia <= 200:
    taxa = 0.50
    passagem = distancia * taxa
else:
    taxa = 0.45
    passagem = distancia * taxa

print(f'A distância de sua viagem é de {distancia:.2f}Km.')
print(f'O valor da passagem será de R${passagem:.2f}')
print(f'\033[1;32mTenha uma ótima viagem!')