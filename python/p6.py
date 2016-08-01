def compute():
  ans = 0
  sumsq = 0
  sqsum = 0
  for i in range(1,101):
    sumsq += i**2
    sqsum += i
  sqsum = sqsum**2
  ans = sqsum - sumsq
  return ans

if __name__ == "__main__":
  print(compute())
