name=input("Enter employee name:")
salary=float(input("Enter Salary:"))
rating=int(input("Enter performance rating(1-5):"))
if rating==5:
    bonus=salary*0.20
elif rating==4:
    bonus=salary*0.15
elif rating==3:
    bonus=salary*0.10
else:
    bonus=0
final_salary=salary+bonus
print("\nEmployee Name:",name)
print("performance Rating:",rating)
print("Bonus amount:",bonus)
print("Final_Salary:",final_salary)
    
           
