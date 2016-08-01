def isPalindrome(s):
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
def isPrime(n):
  i = 1
  origN = n
  while (n>1):
    i+=1
    while(n%i==0):
      n /= i
  return i==origN

