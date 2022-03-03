rows = int(input("enter the size of the pattern : "))
for j in range(1, rows+1):
    print("* " * j)
for i in range(rows + 1, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print(" ")
