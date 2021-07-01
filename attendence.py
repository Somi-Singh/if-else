held=int(input("enter the number"))
attendence=int(input("enter the number"))
classes=held/attendence*100
if held>=26:
    total_classes=held-attendence
    print("allow to sit exaim")
elif attendence>=34:
    total_classes=held-attendence
    print("allow to sit exaim")
else:
    print("no allow to sit exaim")