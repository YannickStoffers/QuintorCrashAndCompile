import math
# A function to print all prime factors of 
# a given number n
def primeFactors(n, x):
     
    # Print the number of two's that divide n
    while n % 2 == 0:
        if 2 >= x:
          return 0
        n = n / 2
         
    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3,int(math.sqrt(n))+1,2):
         
        # while i divides n , print i ad divide n
        while n % i== 0:
            print(n)
            if i >= x:
              return 0
            n = n / i
             
    # Condition if n is a prime
    # number greater than 2
    if n > 2:
        if n > x:
          return 0
    return 1

# Driver Program to test above function
n = 2
x = 10

c = 1
while x > 0:
  if primeFactors(c, n):
    print(c, end=" ")
    x-=1
  c+=1
print("\n")
 
# This code is contributed by Harshit Agrawal
