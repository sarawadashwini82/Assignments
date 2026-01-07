def check_attendance(login_time):
    if login_time<9.30:
        return "present"
    elif login_time>=9.30 and login_time<=10.00:
        return "late"
    else:
        return "absent"
print(check_attendance(9.10))
print(check_attendance(9.40))
print(check_attendance(10.20))

        
        
