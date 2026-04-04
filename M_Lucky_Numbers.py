X = input()
Y = input()
x = int(X)
y = int(Y)

check = False

while x<y:
    if x%10 == 4 or x%10 == 7:
        check = True
        print(x)
        x+=1
    
# if check == False:
#     print(-1)


