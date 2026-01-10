n=7
visitors=[]
print("enter the number of vistors:")
for i in range(n):
    visitors.append(int(input()))
for i in visitors:
    print(i)

high=max(visitors)
highest=visitors.index(high)+1
low=min(visitors)
lowest=visitors.index(low)+1
print("highest traffic on day:",highest)
print("lowest traffic on day:",lowest)

    
    
