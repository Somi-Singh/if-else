age=int("enput enter any age")
sex=input("enter married(Y or N)")
if sex=="F" and age>=20 and  age<=60:
    print("only in urban areas")
elif sex=="m" and age>=20 and age<=40:
    print("he may work in anywhere")
elif sex=="m" and age>=40 and age<=60:
    print("he will work in urban areas only")
else:
    print("error")

