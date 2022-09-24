#!/usr/bin/env python
# bagel-baker.py by Deirdre Saoirse Moen <deirdre@deirdre.net>
# if you find this useful, enjoy. If you get this as a homework
# problem (as I did), write it yourself. :)

from random import Random
from time import time

def calcProfit(demand, dozensBaked):
 sold = min(demand, dozensBaked)
 unsold = dozensBaked - sold

 cost = dozensBaked * 3.80
 revenue = (5.40 * sold) + (2.70 * unsold)
 return (revenue - cost)

def main():

 p = []
 for i in xrange(0, 4):
  p.append(0)

 g = Random(time())
 for days in xrange(1,6):
  x = g.random()
  if x < 0.35:
   customers = 8
  elif x < 0.65:
   customers = 10
  elif x < 0.90:
   customers = 12
  else:
   customers = 14

  bagels = 0
  for c in xrange(0, customers):
   y = g.random()
   if y < 0.4:
    bagels = bagels + 1
   elif y < 0.7:
    bagels = bagels + 2
   elif y < 0.9:
    bagels = bagels + 3
   else:
    bagels = bagels + 4

  for c in xrange(1, 5):
   p[c-1] = p[c-1] + calcProfit(bagels, c*10)

  print "Day %s, %s customers, %s dozen ordered" % (days, customers, bagels)
 for c in xrange(1, 5):
  print "Profit for %s dozen bagels: $%7.2f" % (c*10, p[c-1])
  

if __name__ == '__main__':
 main()
