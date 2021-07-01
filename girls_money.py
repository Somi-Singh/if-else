girl=int(input("enter the girl number 1,2,3"))
money=input("enter the money yes give me money")
if girl==1:
    if money=="yes":
        print("girl 1 give me money")
    else:
        print("girl 2 give me money")
elif girl==2:
    if money=="yes":
        print("girl 2 give me money")
    else:
        print("girl 3 give me money") 
elif girl==3:
    if money=="yes":
        print("girl 3 give me money")
    else:
        print("girl 1 give me money")
else:
    print("no any one give me money")