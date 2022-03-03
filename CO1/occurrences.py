string = input("Enter the String : ")
string=string.split(" ")
listed=[]
count=-1
all_count=[]
for i in string:
    if(i not in listed):
        listed.append(i)      
for i in listed:
    count=count+1
    all_count.append(0)
    for j in string:
        if(i == j):
            all_count[count] +=1; 
for i in range(len(listed)):
    print(listed[i], "  :  ",all_count[i])
