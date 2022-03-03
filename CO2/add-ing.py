word = input("enter a word : ")

end = word[-3:]

if(end=="ing"):
    word=word+"ly"
else:
    word=word+"ing"

print(word)

