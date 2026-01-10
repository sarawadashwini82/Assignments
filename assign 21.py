opening_stock=[200,300,400,120]
closeing_stock=[300,700,400,100]
for i in range(len(opening_stock)):
    if closeing_stock[i]>opening_stock[i]:
        print(f"product{i+1}:closeing stock is increased")
    elif opening_stock[i]>closeing_stock[i]:
        print(f"product{i+1}:closeing stock is  reduced")
    else:
        print(f"product{i+1}:no changes in closeing stock")
