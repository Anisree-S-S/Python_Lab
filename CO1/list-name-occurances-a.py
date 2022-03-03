names = []
num = int(input("Enter total size of list : "))
a_count = 0

for j in range(0,num):
    name = input("Input a name {} : ".format(j+1))
    names.append(name)

for name in names:
    count = name.count("a")
    a_count+=count

print(a_count)


