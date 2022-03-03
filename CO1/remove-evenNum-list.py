list1=[]
newList=[]
n= int(input("Enter total size of list"))
for i in range(n):
    ele=int(input("Enter the number "))
    list1.append(ele)
for i in list1:
    if(i%2!=0):
        newList.append(i)
print(newList)
