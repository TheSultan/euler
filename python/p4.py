import euler

def compute():
  ans = 0
  for i in range(100,1000):
    for j in range(i,1000):
      product = i*j
      if product > ans and euler.is_palindrome(str(product)):
        ans = product
  return ans

if __name__ == "__main__":
  print(compute())
