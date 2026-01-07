def calculate_electricity_bill(units):
    if units<=100:
        return units*2
    elif units<=200:
        return(units-100)*4+200
    else:
        return(units-200)*6+600
print(calculate_electricity_bill(40))
print(calculate_electricity_bill(60))
print(calculate_electricity_bill(80))




