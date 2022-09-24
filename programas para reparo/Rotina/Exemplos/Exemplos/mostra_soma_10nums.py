#Ao Usuario
print "---------------------------------------------------------"
print "Programa para calculo somando numeros ateh chegar a 100 os numeros digitados!!!"
print "Criado por Egon Elemar Braun Filho em PYTHON"
print "---------------------------------------------------------"
print
#Declaracao das variaveis
jogar = 1
num_soma = 0
num = 0
soma = 0

#Programa
while jogar == 1:
    while num < 10:
        num_soma = input("Digite um numero!")
        num = num + 1
        soma = soma + num_soma
        if num == 5:
            print "VAMOS LAH SOH MAIS 5 NUMEROS!!!"
        elif num == 9:
            print "SOH MAIS UM NUMERO!!!"
            
    print "Voce ja digitou 10 numeros!"
    print "A soma de todos os numeros que voce digitou deu",soma,"!!!"
    print "Voce quer jogar novamente?"
    print "Digite 1 para sim e 0 para nao."
    jogar = input("> ")
    if jogar == 1:
        num = 0
        soma = 0

print "Jogo finalizado!"

#Ao Usuario
print "---------------------------------------------------------"
print "Programa para calculo somando numeros ateh chegar a 100 100 os numeros digitados!!!"
print "Criado por Egon Elemar Braun Filho em PYTHON"
print "contato: egonbraun@globo.com"
print "---------------------------------------------------------"
