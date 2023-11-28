x = 0
pessoas = []

while x < 4:
    
    nome = input('qual o seu nome?')

    if nome == 'joao':
        continue

    pessoas.append(nome)

    x = x + 1

print(pessoas)

