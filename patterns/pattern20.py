def pattern20(n):
    for i in range(1,n+1):
        # star
        for j in range(i):
            print("*", end=" ")
        # space
        for j in range(2*n-2*i):
            print(" ", end=" ")
        # star
        for j in range(i):
            print("*", end=" ")
        
        print()
    # Lower portion
    for i in range(n-1,0,-1):
        # star
        for j in range(i):
            print("*", end=" ")
        # space
        for j in range(2*(n-i)):
            print(" ", end=" ")

        # star
        for j in range(i):
            print("*", end=" ")
        print()

pattern20(5)