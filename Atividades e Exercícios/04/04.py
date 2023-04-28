m = 0

for z in range(1,6):
    n = int(input('Digite alguns Num: '))
    if n % 2 == 0:
        m += n

print(f'\na soma dos numeros pares é {m}')