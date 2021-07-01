age1=int(input("enter the age"))
age2=int(input("enter the age"))
age3=int(input("enter the age"))
if age1>age2 and age1>age3:
    print("age1 is oldest")
elif age2>age1 and age2>age3:
    print("age2 is oldest")
else:
    print("age3 is oldest")