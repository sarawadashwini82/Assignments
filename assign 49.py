def is_armstrong(num):
    temp=num
    sum=0
    while temp!=0:
        digit=temp%10
        sum+=digit**3
        temp//=10
    return sum==num
print(is_armstrong(143))
