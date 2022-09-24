# pyQuit.py - Keeps track of your smoke-free life.
# by former smoker Rob Andrews on 8/2/2001
######################################################################################
# I'm just knocking some ideas around at this point.
# I quit smoking a few months ago, and it seems my friends are doing the same.
# I read somewhere today that each cigarette not smoked rescues 11 minutes of life.
# pyQuit.py asks the user for a details about a user's experience quitting smoking.
# I plan to add multi-user support, as well as cleaning up this messy code.
# I'd like to make the whole thing object-oriented based around the user.
# I have not yet added the ability for user data to be saved.
# I'm bumping around the idea of piddling around with versions of this 
# coded as CGI, Jython Applets, Python Server Pages, etc. just for fun.
# Once I finish with the internals here, I'll add an interface using something 
# along the lines of wxPython, Tkinter, and PMW.
# Another feature I plan to add is the ability for the user to select a date in 
# the future and be told how much life, money, time, etc. will be wasted by smoking 
# during the time leading up to that point.
# The time reporting is unrefined at this time. My current intention is to add fairly 
# thorough reporting of time, but I have yet to add something along the lines of "You have 
# been smoke-free for 1 year, 3 lunar months, 2 weeks, 5 days, 3 hours, and 59 minutes." 
# Since I have been slapping ideas together in this one file in a brief sitting, 
# I'm sure some of the code is useless, redundant, inefficient, or generally 
# disagreeable. 
#######################################################################################

import time

quitYear = quitMonth = quitDay = quitHour = quitMinute = quitTime = packsPerDay = averagePackCost = smokesInPack = ''

# Get user quit info

# Find out when the user quit smoking.
quitYear = input("Em que ano tu vais parar de fumar?(Ex.: 2001)\n")
quitMonth = input("Em que mes tu vais parar de fumar? (1 ao 12)\n")
quitDay = input("Em que dia tu vais parar de fumar? (1 ao 31)\n")
quitHour = input("Em que horas tu vais parar de fumar? (0 ao 23)\n")
quitMinute = input("Em que minuto tu vais deixar de fumar? (0 ao 59)\n")

# Assemble the pieces into a meaningful unit for calculation.
quitTime = (quitYear, quitMonth, quitDay, quitHour, quitMinute, -1, -1, -1, -1)

# Determine the extent of the self-injury habit.
packsPerDay = input("Quantas carteiras de cigarro voce fuma por dia?\n")
averagePackCost = input("Quando custa o a carteira?\n")
smokesInPack = input("Quantos cigarros vem em cada carteira?\n")

print quitTime
print "Este e o seu numero de pacotes por dia: " + str(packsPerDay)
print "Este e o custo deles: " + str(averagePackCost)
print "Este e o numero de tragadas por pacote: " + str(smokesInPack)

quitTime1 = time.mktime(quitTime)
currentTime = time.time()
timeDifference = currentTime - quitTime1

yourMinutes = timeDifference / 60
yourHours = yourMinutes / 60
yourDays = yourHours / 24
yourWeeks = yourDays / 7
yourLunarMonths = yourWeeks /4
yourYears = yourWeeks / 52

smokesPerDay = packsPerDay * smokesInPack
cigarettesNotSmoked = smokesPerDay * yourDays
addedLife = cigarettesNotSmoked * 11
moneySaved1 = averagePackCost * packsPerDay
moneySaved = moneySaved1 * yourDays
yourTimes = (yourMinutes, yourHours, yourDays, yourWeeks, yourLunarMonths, yourYears)
yourTimesLabels = {'Minutos': yourMinutes, 'horas': yourHours, 'dias': yourDays, 'semanas': yourWeeks, 'meses': yourLunarMonths, 'anos': yourYears}

print "Este sera o tempo de parar: " + str(quitTime1)
print "Este e o atual tempo: " + str(currentTime)
print "Este e a diferenca do tempo de parar ate o tempo atual: " + str(timeDifference)

print "\n"

for timeterm, timevalue in yourTimesLabels.items():
    print '%-10s ==> %d' % (timeterm, timevalue)

print "\n"

print "Voce adiciona " + str(addedLife) + " segundos de vida se parar de fumar."
print "Voce salva R$ " + str(moneySaved) + "se parar de fumar."
print "\n"

print "Voce tem fumado livre por " + str(yourLunarMonths) + " meses."
print "Voce tem fumado livre por " + str(yourWeeks) + " semanas."
print "Voce tem fumado livre por " + str(yourDays) + " dias."
print "Voce tem fumado livre por " + str(yourHours) + " horas."
print "Voce tem fumado livre por " + str(yourMinutes) + " minutos."

dummy1 = raw_input("Programa encerrado. Para sair, tecle ENTER.")
