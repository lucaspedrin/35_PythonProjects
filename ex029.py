velocidade = float(input('Qual é a velocidade atual do carro (km/h)? '))
multa = (velocidade - 80) * 7

if velocidade > 80:
    print('\033[1;31mMULTADO! Você ultrapassou o limite de velocidade!')
    print(f'\033[0;31mValor da multa: R${multa:.2f}')
else:
    print('\033[32mParabéns! você está dirigindo em uma velocidade segura!')
    print('\033[1;34mTenha uma boa viagem!')