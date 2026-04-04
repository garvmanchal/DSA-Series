# Reverse the number

a = int(input("enter the number: "))
rev = 0

while a > 0:
    last_digit = a % 10
    a = a // 10
    rev = (rev * 10)  + last_digit

print(rev)







