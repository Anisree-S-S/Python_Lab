newFile = open("content.txt","a")
newFile.write("Heyyy There we have new text ! \n")
newFile.close()

readFile = open("content.txt","r")
print(readFile.readlines())
readFile.close()
