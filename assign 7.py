Employee_Name=input("Enter your name:")
Employee_Id=input("Enter your id:")
Basic_Salary=float(input("Enter your Salary:"))
HRA=0.20*Basic_Salary
DA=0.10*Basic_Salary
PF=0.12*Basic_Salary
Net_Salary=Basic_Salary+HRA+DA-PF
print("HRA value=",HRA)
print("DA value=",DA)
print("PF value=",PF)
print("Net_Salary value=",Net_Salary)


                    
