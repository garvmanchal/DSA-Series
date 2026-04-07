# # Check if a number is prime or not
from math import sqrt
# n = int(input("enter the number: "))

# count = 0 

# for i in range(1,int(sqrt(n) +1)):
#     if n % i == 0 :
#         count +=1
#         if n // i != i :
#             count+=1
        
# if count == 2 :
#     print("its a prime")
# else :
#     print("its not")


n = int(input("enter the number: "))
factors = []
for i in range(1,int(sqrt(n)+1)):
    if n % i == 0 :
        factors.append(i)
        if n // i != i :
            factors.append(n//i)

print(sorted(factors))
