n=int(input("enter number of terms:"))
a,b=0,1
for i in range(n):
    print(a)
    a,b=b,a+b
