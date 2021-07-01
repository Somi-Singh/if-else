year=int(input("enter any year"))
if year%4==0 and year%100!=0:
    print("it is leap year")
else:
    print("it is not leap year")