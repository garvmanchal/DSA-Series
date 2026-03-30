'''
A 
B B 
C C C 
D D D D 
E E E E E
'''
# def pattern16(n):
#     for i in range(1,n+1):
#         for j in range(i):
#             print(chr(64 + i), end=" ")
#         print()

# pattern16(5)


def pattern16(n):
    for i in range(1,n+1):
        for j in range(i):
            print(chr(ord("@")+ i), end=" ")
        print()

pattern16(5)

