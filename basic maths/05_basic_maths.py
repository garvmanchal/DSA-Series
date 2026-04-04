# Print all divisors
from math import sqrt
a = int(input("enter the number: "))
divisors= []
# for i in range(1,a+1):
#     if a % i == 0 :
#         divisors.append(i)
    
# print(divisors)


for i in range(1,int(sqrt(a) + 1)):
    if a % i == 0:
        divisors.append(i)
        if a//i != i :
            divisors.append(a//i)

print(sorted(divisors))