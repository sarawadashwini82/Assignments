dist=int(input("enter the distance in km:"))
if dist<=5:
    print("local distance")
elif dist>6 and dist<20:
    print("city")
else:
    print("outstation")
    
