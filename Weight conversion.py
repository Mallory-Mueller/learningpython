weight=int(input("weight:"))
unit=input("(l)bs or (K)g:")
if unit.upper() == "L":
   converted = weight *.45
   print(f"You are {converted} kilos")
else:
    converted= weight /.45
    print(f"You are {converted} pounds")