

n = 3
def binary_business(n):
  L = []
  for i in xrange(16):
      b = bin(i)[2:]
      l = len(b)
      b = str(0) * (n - l) + b
      L.append(b)
print L
      
