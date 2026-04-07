# GCD/HCF
n1 = int(input("enter the first number: "))
n2 = int(input("enter the second number: "))

# for i in range(1,min(n1,n2)):
#     if (n1 % i == 0  and n2 % i == 0) :
#         gcd= i

# print(gcd)


for i in range(min(n1,n2), 1,-1):
    if n1 % i == 0 and n2 % i == 0 :
        print(i)
        
        break

