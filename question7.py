qty=int(input("enter any qty"))
a=qty*100
if a>1000:
    print(a*10/100-a)
else:
    print(a)