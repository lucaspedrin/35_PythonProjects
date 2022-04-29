dia = int(input('Quantos dias o carro foi alugado? '))
kmp = float(input('Qual foi a quantidade de km percorridos? '))
aluguel_dia = dia * 60
km_rodados = kmp * 0.15
total = aluguel_dia + km_rodados
print(f'O total a pagar é de: R${total:.2f}')