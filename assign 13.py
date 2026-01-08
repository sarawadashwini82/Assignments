stud=int(input("enter student marks:"))
att=int(input("enter student attendance percentage:"))
if stud>40 and att>75:
    print("student pass")
else:
    print("fail")


username=input("Enter Username:")
Email_id=input("Enter your email_id:")
if username=="ashsru" or Email_id=="krarak@gmail.com":
    print("Login Allowed")
else:
    print("Not Allowed")
    
issuspend=bool(input("Enter true or false :"))
if issuspend==True:
    print(not(issuspend))
