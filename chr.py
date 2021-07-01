chr=input("enter your character")
if chr>="a" and chr<="z":
    print("it is alphabet")
elif chr>="0" and chr<="9":
    print("it is digit")
elif chr=="@":
    print("it is special character")
else:
    print("nothing")