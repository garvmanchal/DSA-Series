''' Armstrong Number :

n = 371 
so when : 3 **3 + 7**3 + 1**3 = 371 , then its an armstrong number
'''


a = int(input("enter the number: "))
dup = a
sum = 0
while a > 0 :
    last_digit = a % 10 
    sum = sum + (last_digit ** 3)
    a = a // 10

if sum == dup :
    print(True)
else :
    print(False)
    
    