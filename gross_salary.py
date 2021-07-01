salary=int(input("enter your salary"))
h_r_a=int(input("enter your h_r_a"))
d_a=int(input("enter your d_a"))
a=salary*h_r_a/100
b=salary*d_a/100
gross_salary=a+b
if salary<=10000:
    print(gross_salary)
elif salary<=20000:
    print(gross_salary)
else:
    print("nothing")