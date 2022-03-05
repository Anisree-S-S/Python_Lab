dict={}
n=int(input("enter the no of elements "))
for i in range(n):
    dict[i]=int(input("enter the element "))
asc=sorted(dict.values())
print(asc)
asc.reverse()
print(asc)
