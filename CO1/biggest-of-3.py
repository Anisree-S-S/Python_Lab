num1= int(input("Enter First Number : "))
num2= int(input("Enter Second Number : "))
num3= int(input("Enter Third Number : "))

array = [num1,num2,num3]
array.sort(reverse=True)
print(array[0])