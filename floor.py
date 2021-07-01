floor=int(input("enter the floor number"))
room=int(input("enter the room number"))
girls=input("enter your yes or no")
if floor==1 and floor==2 and floor==3 and floor==4:
  if room==1 and room==2 and room==3 and room==4:
      if girls=="yes":
          print("girls are living in room")
      elif girls=="no":
          print("no any one living in room")
elif girls=="yes":
    print("girls are living in room")
else:
    print("no any one living in room")