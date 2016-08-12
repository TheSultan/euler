import math, sys
if sys.version_info.major == 2:
	range = xrange

def sqrt(n):
  return int(math.floor(n**0.5))

def is_palindrome(s):
  return s==s[::-1]

# TODO: Doesn't handle negative numbers
def gcd(small,large):
  if (small > large): large, small = small, large
  if (small == 0): return large
  while (small > 0):
    large, small = small, large % small
  return large

def lcm(a,b):
  return a*b/gcd(a,b)

# This approach is terribly slow but works
def is_prime(n):
  if n <= 1: return False
  elif n<=3: return True
  elif n%2==0: return False
  for i in range(3, sqrt(n)+1, 2): 
    if n%i==0: return False
  return True

# Works but too slow for problem 10 onwards
def list_primes_iter(max):
  return (i for i in range(2,max) if isPrime(i))

#TODO: This is correct but very slow. Figure out why. See alternate approach below
#To find all the prime numbers less than or equal to a given integer n by
#  Eratosthenes' method:
#
#  Create a list of consecutive integers from 2 through n: (2, 3, 4, ..., n).
#  Initially, let p equal 2, the smallest prime number.
#  Enumerate the multiples of p by counting to n from 2p in increments of p, and
#  mark them in the list (these will be 2p, 3p, 4p, ... ; the p itself should not
#      be marked).
#  Find the first number greater than p in the list that is not marked. If there
#  was no such number, stop. Otherwise, let p now equal this new number (which is
#      the next prime), and repeat from step 3.
def list_primes_set(max):
  from collections import OrderedDict
  #TODO: change to generator expression
  
  primes = OrderedDict(dict(zip(range(2, max), [1]*(max-1))))   # dict from prime candidate to 1
  p = 2
  while True:
    for i in range(2*p, max, p):
      primes.pop(i, None)   # deleting preserves order per spec, pop ignores missing
    for key in primes:
      if (key > p):
        p = key
        break
    else:
        break
  return primes

def list_primes(max):
  prime = [True] * max
  prime[0] = prime[1] = False
  for p in range(sqrt(max)+1):
    if prime[p]:
      for m in range(2*p, max, p):
        prime[m] = False
  return [i for (i, isprime) in enumerate(prime) if isprime]
