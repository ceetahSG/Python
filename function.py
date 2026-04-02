
def sum(num1,num2):
    result = num1+num2
    return result
def mul(num1,num2):
    result = num1*num2
    return result

Num1 = input("Enter first number:")
Num2 = input("Enter first number:")
num1 = int(Num1)
num2 = int(Num2)
ans1 = sum(num1,num2)
ans2 = mul(num1,num2)

print("sum:",ans1,"mul:",ans2)
