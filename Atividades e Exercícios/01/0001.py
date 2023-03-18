sexo = 'F' or 'M'

while True:
    sexo = input('Qual o seu gênero? [M(masculino)/F(femenino)]').upper()
    if sexo == 'F' or sexo == 'M':
        break
    else:
        print('Digite novamente')
        sexo = input('M ou F: ').upper()