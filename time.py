time=float(input("enter your time"))
if time>=6.15 and time<=7.00:
    print("morning exersise")
elif time>=7.00 and time<=8.30:
    print("breakfast time") 
elif time>=8.31 and time<=1.00:
    print("coding time") 
elif time>=1.01 and time<=3.00:
    print("lunch time")
elif time>=3.01 and time<=5.00:
    print("english time")
elif time>=5.00 and time<=6.30:
    print("milk time") 
else:
    print("sleeping")