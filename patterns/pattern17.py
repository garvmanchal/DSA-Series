'''
        A
      A B A
    A B C B A 
  A B C D C B A 
A B C D E D C B A  

'''
def pattern17(n):
    for i in range(1,n+1):
        # space
        for j in range(n-i):
            print(" ", end=" ")

        # chr
        ch = 65
        breakpoint = i
        for j in range(1,2*i):
            print(chr(ch) , end=" ")

            if j < breakpoint:
              
             ch +=1

            else :
                ch-=1

        # space
        for j in range(n-i):
            print(" ", end=" ")

        print()

pattern17(5)
 