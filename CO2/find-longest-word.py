num=int(input("Enter the total no.of word : "))
longest = 0
list1=[]
for i in range(num):
    word = input("enter a word : ")
    length = len(word)
    list1.append(word)
    if(length>longest):
        longest=length

list1.sort(reverse=True,key=len)
print(list1)
print("Longest word is {} , has {} letters long".format(list1[0],longest))
