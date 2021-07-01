day=input("enter any num")
meal=input("enter any meal")
if day=="monday":
    if meal=="breakfast":
        print("poha")
    elif meal=="lunch":
        print("rajma chawal")
    else:
        print("roti sabji")
elif day=="tuesday":
    if meal=="breakfast":
        print("poori sabji")
    elif meal=="lunch":
        print("thukpa")
    else:
        print("chicken chawal")
else:
    print("aur kisi din hum daal roti sabji khayengeh")