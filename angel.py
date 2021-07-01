angle1=int(input("enter the number"))
angle2=int(input("enter the number"))
angle3=int(input("enter the number"))
if angle1>=angle2 and angle1<=angle3:
    print("it is obtuse")
elif angle2>=angle1 and angle2<=angle3:
    print("it is ocute")
else:
    print("not anything")