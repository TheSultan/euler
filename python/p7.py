import euler

def compute():
  n = 10001
  i = 2
  primes = 0
  while (primes < n):
    if (euler.is_prime(i)): 
      primes += 1
    i += 1
  return i-1

if __name__ == "__main__":
  print(compute())
