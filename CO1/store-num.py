list = []

for x in range(3):
    num = int(input("Enter an Integer : "))
    if(num>100):
        list.append("over")
    else:
        list.append(num)

print(list)
