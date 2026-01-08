wallet_amt=float(input("enter your wallet amount :"))
shop_amt=float(input("enter your shopping amount:"))
if wallet_amt>=shop_amt:
    wallet_amt-=shop_amt
    print("updated wallet amt:",wallet_amt)
else:
    print("insufficient amount")


score=200
points_earned=int(input("enter your earned socre:"))
score+=points_earned
print("updated score:",score)



stock=int(input("enter total number of stocks:"))
sales=int(input("enter number of stocks are saled:"))
stock-=sales
print("reduced stock after sales:",stock)

