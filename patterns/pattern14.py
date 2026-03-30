'''
A
AB
ABC
ABCD
ABCDE
'''

# method 1 : without ASCII

# def pattern14(n):
#     Letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#     for i in range(1,n+1):
#         for j in range(i):
#             print(Letter[j], end="")
#         print()

# pattern14(5)


# Method 2 : with ASCII

# def pattern14(n):
#     for i in range(1,n+1):
#         for j in range(i):
#             print(chr(65+j) , end="") # A= 65 (ASCII value of A)
#         print()

# pattern14(5)/
#
# METHOD 3 : CHR(ORD)
def pattern14(n):
    
    for i in range(1,n+1):
        for j in range(i):
            print(chr(ord('A') + j), end=" ")
        print()
    
pattern14(5)
