'''
E
DE
CDE
BCDE
ABCDE

'''


def pattern18(n):
    
    for i in range(1,n+1):
        start = ord("E") - i
        for j in range(start, ord("E") + 1):
             print(chr(j), end="")
            

        print()

pattern18(4)
