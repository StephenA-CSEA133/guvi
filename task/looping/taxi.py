def bo():
    s=int(input("Enter Source :"))
    d=int(input("Enter Destination :"))
    t=d-s
    choice(t);
def choice(a):
    if(a>0):
        print("")
        print("1.Mini 2.Macro 3.Prime")
        c=int(input("Make Your Choice :"))
        if(c==1):
            mini(a);
        if(c==2):
            macro(a);
        elif(c==3):
            prime(a);
        else:
            print("Invalid")
            choice(a);
    else:
        print("Invalid")
        print("")
        bo();
def mini(a):
    print("")
    print("Total cost :",a*10)

def macro(a):
    print("")
    print("Total cost :",a*20)

def prime(a):
    print("")
    print("Total cost :",a*30)
rt=1
while(rt==1):
    bo();
    z=int(input("Do you want to continue ? (1.Yes/2.No)"))
    if(z==2):
        print("Thnak you !")
        rt=0
    
    



