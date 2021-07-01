a=int(input("enter 2nd minimum"))
b=int(input("enter 2nd minimum"))
c=int(input("enter 2nd minimum"))
if a>b and a<c or a<b and a>c:
    print("a 2nd minimum")
elif b>a and b<c or b<a and b>c:
    print("b 2nd minimum")
elif c>a and c<b or c<a and c>b:
    print("c 2nd minimum")
else:
    ("nothing")