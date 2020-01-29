import random

b=random.randrange(0,10)

def guess(x,c):
    
    if(c!=4):
        
        n=int(input("Guess the number:"))
        if(x==n):
            print("You WIN")
        else:
            print("Try again")
            c=c+1
            guess(x,c);

    else:
        print("You LOSE")
        print("The Number is :",b)
c=1
guess(b,c);

