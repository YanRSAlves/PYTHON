#Shell script developed by Marc Soler & DaRkWoLf
import sys
import os
import os.path
os.listdir
print "              _   _           ____  _   _  _____"
print "    /\       | | (_)         |  _ \| \ | |/ ____|"
print "   /  \   ___| |_ ___   _____| |_) |  \| | |"
print "  / /\ \ / __| __| \ \ / / _ \  _ <| . ` | |"
print " / ____ \ (__| |_| |\ V /  __/ |_) | |\  | |____"
print "/_/    \_\___|\__|_| \_/ \___|____/|_| \_|\_____| ®"
print "*************************************************"
print "Shell Script v.05b - Developed by : DarKWoLf & Marc Soler \n"
print 'Seja bem-vindo à shell publica da ActiveBNC'
print 'Na compra de 5 BNCs leve um grátis! 6 pelo preço de 5'
print 'Para mais informações, visite o site www.tfa-gaming.com/activebnc ou entre no canal #ActiveBNC da rede Quakenet no IRC - Obrigado.\n'
print '*************************************************'
print '*          Que tarefa deseja realizar?          *'
print '*************************************************'
print '* 1 - Encomendar uma ou mais BNCs?              *'
print '* 2 - Renovar o aluguer de uma ou mais BNCs?    *'
print '* 3 - Ver informações acerca da ActiveBNC?      *'
print '* 4 - Consultar informações de ajuda de BNCs?   *'
print '* 5 - Creditos?                                 *'
print '* 6 - Sair?                                     *'
print '*************************************************\n'
resposta_tarefa = int(raw_input('Escolha o número correspondente à sua tarefa desejada! \n-> '))
print ' '
if resposta_tarefa == 1:
    x = 0
    while x <> 1 :
        print 'Processo de encomenda... Preencha abaixo o inquérito! (Todos os dados referidas são obrigatórios!)'
        nome = raw_input('Digite o seu nome completo : ')
        mail = raw_input('Digite o seu email : ')
        tlm = raw_input('Digite o seu número telefone : ')
        bnc = raw_input('Quantos BNCs deseja encomendar? ')
        print ' '
        print 'Confirme os seus dados : \n'
        print 'Nome : ' + nome
        print 'EMail : ' + mail
        print 'Número telefone : ' + tlm
        print 'BNCs desejadas : ' + bnc
        print ' '
        x = int(raw_input('Estes dados estão correctos? (Yes [1] / No [2]) \n'))
        print 'Os seus dados foram enviados. Será contactado por email...'
        print 'Entretanto já poderá efectuar o pagamento para este NIB: 0035 0171 00195068700 27'
        print 'Total a pagar ' + bnc*1 + '€'
        print 'Após este pagamento, deverá enviar um mail para: marcsoler50@hotmail.com com o seu NIB e montante enviado!\n'
        print 'Obrigado!'
        import os
        import os.path
        os.chdir(r'windows/temp')
        os.mkdir('Aluguer')
        os.mkdir
        os.path.isdir('Aluguer')
        os.listdir('Aluguer')
#Também pode ser gravado com extensão.doc
        os.chdir(r'windows/temp/aluguer')
        f = open('Aluguer.txt' , 'a')
        f.write('Nome : '+nome + '\n')
        f.write('Email : '+mail + '\n')
        f.write('Telefone : '+tlm +'\n')
        f.write('Numero de BNC(s) desejadas : '+bnc+ '\n')
        f.write('\n ')
        f.close()
elif resposta_tarefa == 2 :
     x = 0
     while x <> 1 :         
        print 'Processo de renovação... Preencha abaixo o inquérito! (Todos os dados referidas são obrigatórios!)'
        nome2 = raw_input('Qual o seu nome? ')
        mail2 = raw_input('Qual o seu email? ')
        bnc2 = raw_input('Quantas BNCs tem para renovar? \n')
        print 'Confirme os seus dados : \n'
        print 'Nome : ' +nome2
        print 'Email : ' +mail2
        print 'BNCs para renovar : ' + bnc2
        print ' '
        x = int(raw_input('Estes dados estão correctos? (Yes [1] / No [2]) '))
        print 'Os seus dados foram enviados. Será contactado por email...'
        print 'Entretanto já poderá efectuar o pagamento para este NIB: 0035 0171 00195068700 27'
        print 'Total a pagar ' + bnc2*1 + '€'
        print 'Após este pagamento, deverá enviar um mail para: marcsoler50@hotmail.com com o seu NIB e montante enviado!\n'
        print 'Obrigado!'
        import os
        import os.path
        os.chdir(r'windows/temp')
        os.mkdir('Renovação')
        os.mkdir
        os.path.isdir('Renovação')
        os.listdir('Renovação')
#Também pode ser gravado com extensão.doc
        os.chdir(r'windows/temp')
        f = open('Renovação.txt' , 'a')
        f.write('Nome : '+nome2 + '\n')
        f.write('Email : '+mail2)
        f.write('Numero de BNC(s) desejadas : '+bnc2)
        f.write('\n ')
        f.close()
elif resposta_tarefa == 3:
    print 'Descrição em breve... Mais info em www.tfa-gaming.com/activebnc\n'
elif resposta_tarefa == 4:
    print 'Ajuda em breve, caso urgência contacte-nos no canal #ActiveBNC na Quakenet no IRC, ou entao pelo mail: marcsoler50@hotmail.com'
elif resposta_tarefa == 5:
    print 'Shell Script desenvolvido por : Marc Soler e DaRkWoLf em Python'
elif resposta_tarefa == 6:
   exit()
else:
    print 'Inválido - Reinicie a aplicação!'

