#!/usr/bin/python

# This approach is terribly slow but works

def isPrime(n):
  i = 1
  origN = n
  while (n>1):
    i+=1
    while(n%i==0):
      n /= i
  return i==origN

def compute():
  n = 10001
  i = 2
  primes = 0
  while (primes < n):
    if (isPrime(i)): 
      primes += 1
    i += 1
  return i-1

if __name__ == "__main__":
  print(compute())
