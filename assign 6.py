Name=input("Enter your name:")
Age=int(input("Enter your age:"))
Email_ID=input("Enter your email id:")
Contact_Number=input("Enter your Contact Number:")
Graduation=float(input("Enter your percentage:"))
if Age>=18:
    if Graduation>=60:
        if len(Contact_Number)==10:
            print("intern eligible")
        else:
            print("Contact number must be of 10 digits")
    else:
        print("Percentage must be above 60")
else:
    print("Age must be greater than 18")
        
        
        
