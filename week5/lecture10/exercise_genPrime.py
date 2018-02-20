'''
def genPrimes2():
    primes=[]
    my_prime=1
    while True:
        my_prime+=1
        isprime=True
        for n in primes:
            if my_prime%n==0:
                isprime=False
                break
        if isprime:
            primes.append(my_prime)
            yield my_prime

def genPrimes3():
    """ generator for prime numbers """

    def isPrime(number):
        """ Returns True when number is prime, False otherwise """
        for p in primeList:
            if number%p == 0:
                return False
        return True

    primeList = []
    number = 1
    while True:
        number += 1
        if isPrime(number):
            primeList.append(number)
            yield number
'''
myprimes = [1]

def isPrime(number):
  """ Return when number is prime, False otherwise """
  for prime in myprimes:
    if (number % prime) == 0:
      return False
  return True

def genPrimes():
  """ generator for prime numbers """
  number = 1
  while True:
    number += 1
    if isPrime(number):
        myprimes.append(number)
        print('Prime: ' + str(number))
        # yield number
    if number == 100:
      break

genPrimes()