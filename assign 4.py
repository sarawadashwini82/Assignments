def check_password_strength(password):
    dig=0
    spl=0
    if len(password)<8:
        return "weak password:minimum 8 characters are required"
    for char in password:
        if char>='0' and char<='9':
            dig=1
        elif not((char>='a' and char<='z')or (char>='A' and char<='Z')):
            spl=1
    if dig==0:
        return "weak password:because digit is missing"
    if spl==0:
        return "weak passwod:because special chracter is missing"
    return "strong password"
print(check_password_strength("ash"))
print(check_password_strength("ash@1234"))
