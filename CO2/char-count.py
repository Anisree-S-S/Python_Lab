
word=str(input("Enter the string: "))
freq={}

for letter in word:
    if letter in freq:
        freq[letter]+=1
    else:
        freq[letter]=1
print("The frequency of characters in",word,":",str(freq))
