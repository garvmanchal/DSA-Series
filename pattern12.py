'''
1             1 
1 2         2 1 
1 2 3     3 2 1 
1 2 3 4 4 3 2 1 
'''  
def pattern12(n):
    for i in range(1,n+1):
            # num
            for j in range(1,i+1):
                print(j, end=" ")
            

            # space
            for j in range(2*n - 2*i):
                print(" ",end=" ")

            # number
            for j in range(i,0,-1):
                print(j, end=" ")
            
            print()
        
pattern12(4)
               
