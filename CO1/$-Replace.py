word = input("Please enter your word : ")
first_char = word[0]
word = word.replace(first_char,"$")
word = first_char+word[1:]
print(word)