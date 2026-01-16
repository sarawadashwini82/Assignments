stud={}
def add_stud(name,marks):
     #name=input("enter the name of the student:")
     #marks=float(input("enter the student marks:"))
     stud[name]=marks
     print("student added successfully")
def update_stud():
         name=input("enter the student name to update marks:")
         if name in stud:
             marks=float(input("enter the marks of the student:"))
             stud[name]=marks
             print("updated successfully")
         else:
             print("required student not found")
     #update_stud()
def view_stud():
    if not stud:
             print("no student records available")
    else:
             for name,marks in stud.items():
                 print(name,":",marks)
      #view_stud()
n=int(input("enter the number of students:"))
for i in range(n):
    name=input("enter the name of student:")
    marks=float(input("enter the students marks:"))
    add_stud(name,marks)
update_stud()
view_stud()
                
      
      

                
             
