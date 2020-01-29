s=int(input("Enter starting value:"))
e=int(input("Enter ending value:"))
prime=0

for i in range(s,e+1):
    val=1 
    for j in range(2,i):
        if(i%j==0):           
           val=0
    if(val==1 and i!=1):
        prime = prime + i
print(prime)
