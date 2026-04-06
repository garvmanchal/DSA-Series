# check Palindrome 
# for this we have to create a duplicate and then after reversing it we will match it to the rev one

a = int(input("enter the number: "))
dup = a
rev = 0 

while a > 0 :
    last_digit = a % 10 
    a = a // 10
    rev = (rev*10)+ last_digit

print(rev)
if dup == rev :
    print("Its an palindrome number")
else :
    print(False)
