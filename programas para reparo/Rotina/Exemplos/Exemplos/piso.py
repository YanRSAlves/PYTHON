#Ao Usuario
print "---------------------------------------------------------"
print "Programa para calculo de piso!"
print "Criado por Egon Elemar Braun Filho em PYTHON"
print "---------------------------------------------------------"
print
#Declaracao das variaveis
piso = 0
num = 0
calc = 1

#Programa
while calc == 1:
    num = input("Informe um numero para a pesquisa de seu PISO. > ")
    while piso <= num:
        piso = piso + 1

    piso = piso - 1
    print "O piso do numero",num,"eh",piso
    print
    print "Deseja calcular novamente?"
    print "Digite 1 para sim e 0 para nao."
    calc = input("> ")
    if calc == 1:
        piso = 0
        num = 0

print "Programa Finalizado!"

#Ao Usuario
print "---------------------------------------------------------"
print "Programa para calculo de piso!"
print "Criado por Egon Elemar Braun Filho em PYTHON"
print "contato: egonbraun@globo.com"
print "---------------------------------------------------------"
