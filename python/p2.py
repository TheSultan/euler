#!/usr/bin/python

def compute():
  x,y = 1,2
  max = 4*10**6
  sum = 0
  while (x <= max): 
    if (x%2 == 0) : 
      sum += x
    x,y = y, x+y
  return str(sum)

if __name__ == "__main__":
  print(compute())
