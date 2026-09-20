# Extraction of numbers 


n = int(input("enter the number: "))


while(n > 0):
    last_digit = n % 10 
    print(last_digit)

    n = n // 10
    print(n)    


# count the digits 

n = int(input("enter the value : "))
count = 0

while (n > 0):
    n = n // 10
    count +=1

print(count)


# another method to find out count of the digits
from math import log10

n = int(input("enter the value: "))

count = int(log10(n)+1)
print(count)

