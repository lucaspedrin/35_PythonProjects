from math import radians, sin, cos, tan

ang = float(input('Digite o valor do ângulo: '))
rad = radians(ang)

sen = sin(rad)
cos = cos(rad)
tan = tan(rad)

print(f'O seno de {ang} é: {sen:.2f}\nO cosseno de {ang} é: {cos:.2f}\nA tangente de {ang} é: {tan:.2f}')