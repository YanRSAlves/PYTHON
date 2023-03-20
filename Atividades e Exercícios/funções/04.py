x = int(input('Qual a sua nota no mestrado: '))

def nota():
    global x
    if x >= 100:
        print('Conceito A')
    elif x >= 80:
        print('Conceito B')
    elif x >= 70:
        print('Conceito C')
    elif x >= 60:
        print('Conceito D')
    elif x >= 40:
        print('Conceito E')
    else:
        print('Cuidado chama o Chris')

nota() 