#Ao Usuario
print "---------------------------------------------------------"
print "Programa para calculo de Areas!"
print "Criado por Egon Elemar Braun Filho em PYTHON"
print "---------------------------------------------------------"
print

#Declaracao de Variaveis
calc = 1
forma = 1
area = 0
lado = 0

#Programa
while calc == 1:
    print "Escolha qual objeto!"
    print " 1 Quadrado"
    print " 2 Circunferencia"
    print " 3 Retangulo"

    forma = input("> ")

    if forma == 1:
        lado = input("Lado 1 = ")
        area = lado**2
        print "A area do Quadrado eh", area
    elif forma == 2:
        raio = input("raio = ")
        area = 3.14*(raio**2)
        print "A area da circunferencia eh",area
    elif forma == 3:
        lado1 = input("Lado 1 = ")
        lado2 = input("lado 2 = ")
        area = lado1*lado2
        print "A area do retangulo eh", area
    else:
        print "Voce digitou um objeto naum valido!"

    print "Voce deseja calcular novamente?"
    print "Digite 1 para sim e 0 para nao."
    calc = input("> ")
    if calc == 1:
        forma = 1
        area = 0
        lado = 0

print "Programa Finalizado!"

#Ao Usuario
print "---------------------------------------------------------"
print "Programa para calculo de Areas!"
print "Criado por Egon Elemar Braun Filho em PYTHON"
print "---------------------------------------------------------"
