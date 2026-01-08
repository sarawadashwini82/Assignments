course=input("Enter course name:")
if course=="Python Programming":
    fee=5000
elif course=="Data Analytics":
    fee=8000
elif course=="AI and ML":
    fee=12000
else:
    print("invalid course selected")
    exit()
student_discount=fee*0.10
early_discount=fee*0.05
total_discount=student_discount+early_discount
final_amount=fee-total_discount
print("\n course Name:",course)
print("Original fee:",fee)
print("Total Discount:",total_discount)
print("Final payable Amount:",final_amount)
