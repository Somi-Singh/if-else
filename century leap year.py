year=int(input("enter any year"))
if year%4==0 and year%100!=0:
    print("it is leap year")
elif year%4==0 and year%100==0 and year%400==0:
    print("it is century leap year")
else:
    print("not leap year")