list1=[]
list2=[]
l1 = int(input("Enter total size of list1 : "))
l2 = int(input("Enter total size of list2 : "))

for i in range(0,l1):
    name = input("Input the color for list 1 :")
    list1.append(name)

for i in range(0,l2):
    name = input("Input the color for list 2 :")
    list2.append(name)

print("Not Repeated Color are :")
print([item for item in list1 if item not in list2])
