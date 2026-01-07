def calculate_discount(price,customer_type):
    if customer_type=="regular":
        return price-(price*0.05)
    elif  customer_type=="premium":
        return price-(price*0.15)
    elif  customer_type=="employee":
        return price-(price*0.25)
    else:
        return price
print(calculate_discount(2000,"regular"))
print(calculate_discount(200,"premium"))
print(calculate_discount(1000,"employee"))    
