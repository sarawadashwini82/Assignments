num=int(input("enter number:"))
count=0
while num!=0:
    count+=1
    num//=10
print("number of digits:",count)    
