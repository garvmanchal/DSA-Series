'''
              *
            * * *
          * * * * *
        * * * * * * *
       * * * * * * * * *       
         * * * * * * *      
          * * * * *   
            * * *
              *

'''
def pattern9(n):
    for i in range(1,n+1):
        # space
        for j in range((n+1)-i-1):
            print(" ",end=" ")
        # star
        for j in range(2*i-1):
            print("*", end=" ")
          # space
        for j in range((n+1)-i-1):
            print(" ",end=" ")
            
       
        
        print()

def pattern8(n):
    for i in range(n):
        # space
        for j in range(i):
            print(" ",end=" ")
        # star 
        for j in range(2*n - 2*i -1):
            print("*", end=" ")

        for j in range(i):
            print(" ",end=" ")

        print()
pattern9(5)
pattern8(5)
