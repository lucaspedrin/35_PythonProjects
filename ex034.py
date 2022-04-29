salário = float(input('Qual é o salário mensal do funcionário? R$'))

if salário > 1250:
    aumento = salário + (salário * (10/100))
else:
    aumento = salário + (salário * (15/100))

print(f'O aumento salarial foi de \033[31mR${salário:.2f}\033[m para \033[32mR${aumento:.2f}')