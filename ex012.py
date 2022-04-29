preço = float(input('Qual é o preço do produto? '))
desconto = preço - (preço * 5/100)
print(f'Com desconto de 5% o novo valor é: R${desconto:.2f}')