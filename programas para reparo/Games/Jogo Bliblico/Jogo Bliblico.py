print ('\n'*100)
print (""" 
# *** JOGO BIBLICO *** Algoritmo de Abraao
# By Yan Rocha, apenas uma versâo modificada!

    Neste jogo voce deve convencer a Deus a nao destruir
    Sodoma e Gomorra (Genesis 18:24-32). Algo um tanto
    quanto muito dificil, mas vamos la:

    No prompt "Eu:" Digite:
    --> Senhor, e se houver xyz justos na cidade?
    (Onde 'xyz' corresponde a um numero entre 0 e 999)

    Lembre-se: Digite certo para acabar logo!

    Boa sorte!!!
""")
input('\nTecle <ENTER> ')

# Inicio do jogo
print ('\n'*100)
numjust = 50
while numjust >= 10:
    justos = input('Eu: ')
    try:
        if int(justos[20:23]) == numjust:
            print ("Deus: Nao destruirei a cidade por amor dos",numjust,"justos.")
            if numjust < 45:
                numjust -= 5
            numjust -= 5
    # Jogo do tipo "quente ou frio"
        elif int(justos[20:23]) > numjust:
            print ("Deus: Voce nao deveria pedir por menos justos?")
        elif int(justos[20:23]) < numjust:
            print ("Deus: Voce nao gostaria de pedir por mais justos?")
    # Se digitar errado, comeca tudo de novo
    except ValueError:
        print ("Deus: Acaso vou destruir as cidades sem consultar Abraao?")
        numjust = 50
input('\nTecle <ENTER> ')

# Fim do jogo
print ('\n'*100)
print ("\nDeus: Anjos, tirem Lo e sua familia de la...")
print ("\nAnjos: Sim, Senhor!")
print ("\n\n*** GAME OVER!!! ***\n")
input('\nTecle <ENTER> ')
