import math
def is_prime(n):
    if (math.factorial(n-1)+1) % n!=0:
        print ("NO")
    else:
        print ("YES")
print(is_prime(13))

