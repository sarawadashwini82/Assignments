def check_intern_eligiblity(age,percentage):
    if age>=18 and percentage>=60:
        return "Eligible:age is 18 or above and percentage is 60 or more"
    else:
        return "not eligible:age is less than 18 and percentage is less than 60"
res=check_intern_eligiblity(20,75)
print(res)
res=check_intern_eligiblity(15,55)
print(res)
