# Módulo Seqüências de Fibonacci

def fib(n): # write Fibonacci series up to n
    a,b = 0,1
    while b < n:
          print b,
          a,b = a,a+b
          
def fib2(n): # return Fibonacci series up to n
    result = []
    a,b =  0,1
    while b < n:
          result.append(b)
          a,b = a,a+b
    return result
    
          

