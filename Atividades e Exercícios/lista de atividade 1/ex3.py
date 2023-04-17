#QUESTÃO 3

while True:  
    av1 = int(input('1)Como você avalia o atendimento entre 0 a 5: '))
    if av1 > 5 or av1 < 0:
        av1 = int(input('\nInformação inválida, tente novamente !!!\nComo você avalia o atendimento ente 0 a 5: '))
    else:
        break
while True:  
    av2 = int(input('2)As informações foram do serviço foram repassadas de maneira clara? entre 0 a 5: '))
    if av2 > 5 or av2 < 0:
        av2 = int(input('\nInformação inválida, tente novamente !!!\nAs informações foram do serviço foram repassadas de maneira clara? avale de 0 a 5: '))
    else:
        break
while True:  
    av3 = int(input('3)O nosso serviço está abaixo, acima ou atende suas expectativas? Dê o valor entre 0 a 5: '))
    if av3 > 5 or av3 < 0:
        av3 = int(input('\nInformação inválida, tente novamente !!!\nO nosso serviço está abaixo, acima ou atende suas expectativas? Dê o valor ente 0 a 5: '))
    else:
        break
while True:  
    av4 = int(input('4)Como você avalia o tempo que levou para o serviço ser concluido? entre 0 a 5: '))
    if av4 > 5 or av4 < 0:
        av4 = int(input('\nInformação inválida, tente novamente !!!\nComo você avalia o tempo que levou para o serviço ser concluido? ente 0 a 5: '))
    else:
        break
while True:  
    av5 = int(input('5)Em uma escala de 0 a 5, o qaunto você nos recomendaria para um amigo ou familiar?: '))
    if av5 > 5 or av5 < 0:
        av5 = int(input('\nInformação inválida, tente novamente !!!\nEm uma escala de 0 a 5, o qaunto você nos recomendaria para um amigo ou familiar?: '))
    else:
        break
        
print("\nAtendimento avaliado")
