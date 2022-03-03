lst=[]
x = int(input("enter a four digit number = "))
y = int(input("enter a four digit number = "))
for i in range(x,y):
   for j in range(32,100):
       if i == j*j:
           string = str(i)
           if int(string[0])%2 == 0 and int(string[1])%2 == 0 and int(string[2])%2 == 0 and int(string[3])%2 == 0:
               lst.append(i)
print(lst)
