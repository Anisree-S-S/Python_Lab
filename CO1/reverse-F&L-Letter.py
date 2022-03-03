word = input("Type your word : ")
temp1 = word[0]
temp2 = word[-1]
length = len(word)
result = word[-1]+word[1:length-1]+word[0]
print(result)