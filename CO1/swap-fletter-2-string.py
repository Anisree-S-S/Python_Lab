word = input("Type a string with 2 words seperated by comma : ")
word_list = word.split(" ")
first_letter_1 = word_list[0][0]
first_letter_2 = word_list[1][0]
print(first_letter_2+word_list[0][1:]+" "+first_letter_1+word_list[1][1:])
