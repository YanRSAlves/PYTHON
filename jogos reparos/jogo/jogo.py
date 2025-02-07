import time

resp = "1"
print("Tente adivinhar o número que estou pensando.")
print("Você só tem 5 chances e o número está entre 0 e 100.")

while resp != "0":
    t = time.localtime()
    x = (((t.tm_sec * 3) // 2) + t.tm_min) - t.tm_hour  # Ajustado para o formato correto

    if x > 100:
        x = 100 - (x - 100)
    elif x < 0:
        x = abs(x)

    i = 1

    try:
        a = int(input(f"Tentativa {i}: "))
    except ValueError:
        a = None
        print("Digite um número inteiro válido.")

    while a is not None and a != x and i < 5:
        if a < x:
            print("O número é mais alto (+)")
        else:
            print("O número é mais baixo (-)")

        i += 1

        try:
            a = int(input(f"Tentativa {i}: "))
        except ValueError:
            a = None
            print("Digite um número inteiro válido.")

    if a == x:
        print(f"Você acertou! Parabéns!!! O número era {x}")
    else:
        print("Suas chances acabaram, você perdeu!!!")
        print(f"O número era {x}")

    resp = input("Para jogar de novo aperte 1 - para sair aperte 0: ")