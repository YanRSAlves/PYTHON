#Ao Usuario
print "---------------------------------------------------------"
print "Programa para calculo somando numeros ateh chegar a 100!"
print "Criado por Egon Elemar Braun Filho em PYTHON"
print "---------------------------------------------------------"
print
#Declaracao das variaveis
jogar = 1
total = 0
numero = 0

#Programa
while jogar == 1:
    numero = input("Digite um numero entre 0 e 100. ")
    if numero > 100 :
        print "Voce digitou um numero maior que cem!!!"
        print "Deseja jogar novamente?"
        print "Digite 1 para sim ou 0 para nao!"
        jogar = input ("> ") 
    else:
        total = total + numero
        if total >= 100:
            print "Voce jah chegou a 100!!!"
            print "seu total eh ", total, "!!!"
            print "Deseja jogar novamente? "
            print "Digite 1 sim ou 0 para nao!"
            jogar = input("> ")
            if jogar == 1:
                total = 0
            elif jogar < 0 or jogar > 1:    
                while jogar < 0 or jogar > 1:
                    print "Digite somente 1 ou 0 !!!"
                    print "Deseja jogar novamente? "
                    print "Digite 1 sim ou 0 para nao!!!"
                    jogar = input("> ")
                    if jogar == 1:
                        total = 0

print "Jogo Finalizado!"
print

#Ao Usuario
print "---------------------------------------------------------"
print "Programa para calculo somando numeros ateh chegar a 100!"
print "Criado por Egon Elemar Braun Filho em PYTHON"
print "contato: egonbraun@globo.com"
print "Exemplo pego do site www.scriptbrasil.com.br"
print "---------------------------------------------------------"
