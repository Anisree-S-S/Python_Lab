ele=input('Enter the statement')
vowels=['a','e','i','o','u']
list1=[]
str=ele.lower()
for i in str:
    if(i in vowels and i not in list1):
        list1.append(i)
print("Vowel Present in this statements: ",list1)
