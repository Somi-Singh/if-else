user1=int(input("enter the number"))
user2=int(input("enterr the number"))
user3=int(input("enter the number"))
if user1>user2 and user1>user3:
    print("user1 is maximum")
elif user2>user1 and user2>user3:
    print("user2 is maximum")
else:
    print("user3 is maximum")