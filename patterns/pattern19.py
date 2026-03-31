''''
* * * * * * * * * *
* * * *     * * * *
* * *         * * *
* *             * *
*                 *
*                 *
* *             * *
* * *         * * *
* * * *     * * * *
* * * * * * * * * * 
'''
def pattern19(n):
    for i in range(n):
        # star

        for j in range(n-i):
            print("*" , end=" ")

        # space
        for j in range(i*2):
            print(" ", end=" ")
        # star
        for j in range(n-i):
            print("*" , end=" ")
         
        print()

    for i in range(1,n+1):
        # star
        for j in range(i):
            print("*", end=" ")
        # space
        for j in range(2*n - 2*i):
            print(" ", end=" ")
        # star
        for j in range(i):
            print("*", end=" ")
        print()



pattern19(5)
 
