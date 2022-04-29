nome = str(input('Digite seu nome completo: ')).strip()
silva = 'silva' in nome.lower()
print(f'\033[7;97mSeu nome tem Silva? {silva}\033[m')