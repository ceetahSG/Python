def fullName(first,last,title,**adition):
    name = f'{first} {last} {title} {adition}'
    for key,value in adition.items():
        print(key,value)
    return name
he = fullName(last='khan',first='rahim',title='shorkar',title2='bepari',title3='khondokar')
print(he)

# multiple return

def all(num1,num2):
    sum = num1+num2
    mul = num1* num2
    div = num1 / num2
    
    # return [sum,mul,div]
    return sum,mul,div
result = all(1,2)
print(result)