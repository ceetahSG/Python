numbers = input()
reverseNumbers = numbers[::-1]

check = True
for num in reverseNumbers:
    if num == '0' and check == True:
        continue
    else:
        check = False
        print(num,end="")
print()
if numbers == reverseNumbers:
    print("YES")
else:
    print("NO")