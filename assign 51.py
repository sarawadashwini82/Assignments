def sum_even_odd(lst):
    even_sum=0
    odd_sum=0
    for num in lst:
        if num%2==0:
            even_sum+=num
        else:
            odd_sum+=num
    print("even sum:",even_sum)
    print("odd sum:",odd_sum)
sum_even_odd([1,2,3,4,5])    
        
