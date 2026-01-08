student_list=input("enter the names of students:")
attendance_list=input("enter the names of students to check in attendance list:")
if student_list in attendance_list:
    print("student name exist in the attendance list")
else:
    print("not existed in attendance list")


product=input("enter the products name:")
inventory=input("enter the products to check in inventory:")
if product not in inventory:
    print("product is not found in inventory")
else:
    print("product is found in inventory")
