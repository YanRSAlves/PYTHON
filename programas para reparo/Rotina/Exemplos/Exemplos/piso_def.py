#Ao Usuario
print "---------------------------------------------------------"
print "Programa para calculo de piso!"
print "Criado por Egon Elemar Braun Filho em PYTHON"
print "---------------------------------------------------------"
print

#Declaracao das variaveis
calc = 1

#Funcao
#-------------------------------------------------------------
def piso(number, value):
    while value <= number:
        value = value + 1
            
        resposta = value - 1
    return resposta
#-------------------------------------------------------------

#Programa
while calc == 1:
    num = input("Informe um numero para a pesquisa de seu PISO. > ")  
    res = piso(num, 0)
    print "O piso do numero",num,"eh",res
    print
    print "Deseja calcular novamente?"
    print "Digite 1 para sim e 0 para nao."
    calc = input("> ")
    if calc == 1:
        res = 0
        num = 0
        x = 0
    elif calc < 0 or calc > 1:
        while calc > 1 or calc < 0:
            print "Deseja calcular novamente?"
            print "Digite somente 1 para sim e 0 para nao."
            calc = input("> ")
            
            
print "Programa Finalizado!"

#Ao Usuario
print "---------------------------------------------------------"
print "Programa para calculo de piso!"
print "Criado por Egon Elemar Braun Filho em PYTHON"
print "contato: egonbraun@globo.com"
print "---------------------------------------------------------"
