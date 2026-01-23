def login(username, password):
    if username == "dd_admin" and password == "dd@123":
        print("Login Successful\n")
        return True
    else:
        print("Access Denied")
        return False
uname = input("Enter Username: ")
pwd = input("Enter Password: ")
if not login(uname, pwd):
    exit()
def register_employee():
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    department = input("Enter Department: ")
    basic_salary = float(input("Enter Basic Salary: "))
    if age < 18:
        print("Error: Employee must be at least 18 years old")
        return None
    if basic_salary <= 0:
        print("Error: Salary must be greater than 0")
        return None
    print("Employee Registered Successfully\n")
    return emp_id, name, age, department, basic_salary
employee = register_employee()
if employee is None:
    exit()
def attendance_management():
    present_days = 0
    for day in range(1, 6):
        status = input(f"Day {day} Attendance (P/A): ").upper()
        if status == "P":
            present_days += 1
    if present_days >= 4:
        status = "Regular"
    elif present_days == 3:
        status = "Warning"
    else:
        status = "Irregular"
    print(f"Total Present Days: {present_days}")
    print(f"Attendance Status: {status}\n")
    return present_days
present_days = attendance_management()
def calculate_salary(basic_salary, present_days):
    pf = basic_salary * 0.12
    if present_days < 3:
        hra = 0
        da = 0
    else:
        hra = basic_salary * 0.20
        da = basic_salary * 0.10
    net_salary = basic_salary + hra + da - pf
    return net_salary
net_salary = calculate_salary(employee[4], present_days)
print(f"Net Salary: ₹{net_salary}\n")
def performance_evaluation():
    total = 0
    for i in range(1, 4):
        rating = int(input(f"Enter Rating {i} (1-5): "))
        total += rating
    avg = total / 3
    if avg >= 4:
        result = "Excellent"
    elif avg >= 3:
        result = "Good"
    else:
        result = "Needs Improvement"
    print(f"Average Rating: {avg}")
    print(f"Performance: {result}")
performance_evaluation()
