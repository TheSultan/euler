#!/usr/bin/python

def compute():
  n = 1000
  for a in xrange(1,n):
    for b in xrange(1, n-a):
      c = n - a - b
      if (a**2 + b**2 == c**2):
        return a*b*c
  return ans

if __name__ == "__main__":
  print(compute())
