import random
b=random.randrange(1,3)
def win(r,s):
    if(r==s):
        print("Draw")
    elif(r==1):
        if(s==2):
            print("You Win")
        else:
            print("You Lose")
    elif(r==2):
        if(s==1):
            print("You Lose")
        else:
            print("You Win")
    elif(r==3):
        if(s==1):
            print("You Win")
        else:
            print("You Lose")

w=1
while(w==1):
    print("1.Rock 2.Paper 3.Scissor")  
    u=int(input("Play :"))
    win(b,u)
    q=int(input("Do you want to continue ?(1.Yes/2.No)"))
    if(q==2):
        w=0
