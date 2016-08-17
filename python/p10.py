import euler, operator

def compute():
  primes = euler.list_primes(2*10**6)
  return reduce(operator.add, primes)

if __name__ == "__main__":
  print(compute())
