# Reverse a number

n = int(input("enter the number : "))
rev = 0

while(n>0):
    last_digit = n % 10

    n = n // 10

    rev = (rev * 10) + last_digit

print(rev)


    