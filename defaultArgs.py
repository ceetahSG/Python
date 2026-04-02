def do_sum(num1,num2,*nums):
    sum = 0
    for num in nums:
        sum +=num
    return sum
result = do_sum(1,2,3,4,5,6,7,7,8,9)
print(result)