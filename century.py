year=int(input("enter any year"))
if year<=100:
    print("1st century")
elif year%100==0:
    print(year//100,"century")
else:
    print(year//100+1,"century")