s=int(input("Enter starting value:"))
e=int(input("Enter ending value:"))
sum=0
for i in range(s,e+1):
    if(i%2==0):
        sum=sum+i
print(sum)
