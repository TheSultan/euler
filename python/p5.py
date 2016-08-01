import euler

def compute():
  return reduce(euler.lcm, range(1,20))

if __name__ == "__main__":
  print(compute())
