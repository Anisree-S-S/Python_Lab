d1={}
d2={}
n1=int(input("Enter the size dictionary 1: "))
n2=int(input("Enter the size dictionary 2: "))
for i in range(n1):
    key=input("Enter the key dict 1:")
    value=input("Enter the value:")
    d1[key]=value
for i in range(n2):
    key=input("Enter the key dict 2:")
    value=input("Enter the value:")
    d2[key]=value

d1.update(d2)
print(d1)
