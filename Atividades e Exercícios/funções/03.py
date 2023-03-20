limite = int(input('Qual limite deseja definir: '))

def dois_valores(x,y):
    global limite
    restante = limite - (x+y)
    if (x+y)<= limite:
        print('\033[0;34;46mCompras Aprovadas\033]m')
        print(f'ainda tem R${restante} de limite')
        if (x+y)<= limite/2:
            print('nem chegou na metade pode gastar!')
    elif (x + y) > limite:
        print('\033[0;31;44mCompras Recusadas\033]m')
    else:
        print('Deu ruim no sistema ligue para um Gerente! URGENTE! ')

dois_valores(1200,500)