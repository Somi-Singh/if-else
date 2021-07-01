kitchen_team=int(input("enter the number 1,2,3"))
health= input("enter your health  well,not well")
if kitchen_team==1:
    if health=="well":
        print("kitchen_team 1 work")
    else:
        print("kitchen_team 2 work")

elif kitchen_team==2:
    if health=="well":
        print("kitchen_team 2 work") 
    else:
        print("kitchen_team 3 work")
elif kitchen_team==3:
    if health=="well":
        print("kitchen_team 3 work")
    else:
        print("kitchen_team 1 work")
else:
    print("no any one work")