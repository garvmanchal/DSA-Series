'''
A B C D E 
A B C D 
A B C 
A B 
A
'''

# def pattern15(n):
#     Letter = "ABCDE"
#     for i in range(n) :
#         for j in range(n-i):
#             print(Letter[j], end="")
#         print()

# pattern15(5)

def pattern15(n):
    for i in range(1,n+1):
        for j in range(ord('A'), ord('A') + (n-i+1)):
            print(chr(j),end=" ")
        print()

pattern15(5)


