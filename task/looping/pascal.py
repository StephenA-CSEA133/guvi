def pat():
    n=int(input("Enter the range :"))
    for i in range(1,n+1):
        for j in range(i,n):
            print(" ",end=" ")
        for k in range(1,i):
            print(k,end=" ")
        for l in range(i,0,-1):
            print(l,end=" ")
        print()
pat()
