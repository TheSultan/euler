#!/usr/bin/python

def compute():
  ans = 0
  i = 1
  n = 600851475143
  while (n>1):
    i+=1
    while (n%i == 0):
      n /= i
  ans = i
  return ans

if __name__ == "__main__":
  print(compute())
