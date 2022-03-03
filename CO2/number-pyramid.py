n = int(input("Enter the range for step pyramid : "))

for i in range(n):
    s = ""
    for j in range(i+1):
        s = s+" "+str((i+1)*(j+1))

    print(s)


