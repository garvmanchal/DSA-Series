# count the digit

#  if the number of iteration is division then its time complexity comes in Big O(log10(n))
a = int(input("enter the number : "))
num = 0

# way 1
while a > 0 :
    last_digit= a % 10
    num+=1
    a = a // 10
print(num)


# way 2
from math import log10
num = int(log10(a)+ 1)
print(num)
