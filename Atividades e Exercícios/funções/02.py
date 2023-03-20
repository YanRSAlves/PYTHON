def valores(x,y):
    if x < y:
        print(f'o maior é {y}')
    elif x > y:
        print(f'o maior é {x}')
    else:
        print('Os valores são iguais')
    
valores(10,20)
valores(30,10)
valores(12,12)