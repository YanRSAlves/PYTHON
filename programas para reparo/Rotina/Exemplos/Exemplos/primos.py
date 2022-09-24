#Ao Usuario
print "---------------------------------------------------------"
print "Programa para calculo do Metodo Euclides!!!"
print "Criado por Egon Elemar Braun Filho em PYTHON"
print "---------------------------------------------------------"
print

#Declaracao das variaveis
candidatos = range(2,100)
base = 2
num = base
resultado = [1]

#Funcoes
#-------------------------------------------------------------

#-------------------------------------------------------------
    
#Programa
while candidatos:
    while num < 100:
        if num in candidatos:
            candidatos.remove(num)
            
        num = num + base

    base = candidatos[0]
    num = base
    resultado.append(candidatos[0])
    del candidatos[0]

print
print ESTE SAO OS NUMEROS PRIMOS ENTRE 1 E 100!!!
print
print resultado

#Ao Usuario
print "---------------------------------------------------------"
print "Programa para calculo de piso!"
print "Criado por Egon Elemar Braun Filho em PYTHON"
print "contato: egonbraun@globo.com"
print "---------------------------------------------------------"
