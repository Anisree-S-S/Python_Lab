# a1 = {'a':1, 'b':13, 'd':4, 'c':2, 'e':30}

# a1_sorted_keys = sorted(a1, key=a1.get, reverse=True)
# a1_sorted_keys_2 = sorted(a1, key=a1.get)

# print(a1_sorted_keys)
# print(a1_sorted_keys_2)

d={}
n=int(input("Enter the elements"))
for i in range(n):
    key=input("Enter the key: ")
    value=int(input("Enter the value in numeric: "))
    d[key]=value
print(d)

d_rev=sorted(d, key=d.get, reverse=True)
d_nrev=sorted(d,key=d.get)
print("Decending Order",d_rev)
print("Ascending Order",d_nrev)
