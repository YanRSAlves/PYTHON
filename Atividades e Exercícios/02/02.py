valor = float(input("Digite o valor do produto: "))

categoria = input("Digite a categoria do produto (A, B ou C): ").upper()

if categoria == "A":
    valor_com_desconto = valor * 0.8  # desconto de 20%
elif categoria == "B":
    valor_com_desconto = valor * 0.9  # desconto de 10%
elif categoria == "C":
    valor_com_desconto = valor * 0.7  # desconto de 30%
else:
    print("Categoria inválida. Tente novamente.")
    valor_com_desconto = valor

print("O valor com desconto é R$ %.2f" % valor_com_desconto)
