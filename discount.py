quantity1=int(input("enter the quantity"))
quantity2=int(input("enter the quantity"))
discount1=quantity1/100*5
discount2=quantity2/100*15
if quantity1>=800:
  total_cost1=quantity1-discount1
  print("total_cost1",total_cost1)
if quantity2>=1000:
  total_cost2=quantity2-discount2
  print("total_cost2",total_cost1)
else:
  print("no discount")