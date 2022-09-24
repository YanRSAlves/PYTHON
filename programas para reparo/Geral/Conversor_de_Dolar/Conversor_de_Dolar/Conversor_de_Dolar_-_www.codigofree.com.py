# Conversor de Dólar
# http://www.codigofree.com
# Criado por Anderson Ferreira (andersonferreira631@yahoo.com.br)

# Abaixo encontra-se o script de um Conversor de Dólar, bastante simples.

# A letra "d" indica o valor do dólar.
# O número "10" indica o valor (de 0 á 10) que será convertido de Dólar para Reais.



# ---------------- #
# Início do Script
# ---------------- #


d = 2.2939989

for p in range(10): print 'US$ %5.2f = R$ %5.2f' % (p, p * d)
print '-' * 20


# ---------------- #
# Fim do Script
# ---------------- #