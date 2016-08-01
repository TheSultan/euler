#!/usr/bin/python

# TODO: Doesn't handle negative numbers
def gcd(small,large):
  if (small > large): large, small = small, large
  if (small == 0): return large
  while (small > 0):
    large, small = small, large % small
  return large

def lcm(a,b):
  return a*b/gcd(a,b)

def compute():
  return reduce(lcm, range(1,20))

if __name__ == "__main__":
  print(compute())
