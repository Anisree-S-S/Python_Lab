class Rectangle:
    def __init__(a, length, breadth):
        a.length = length
        a.breadth = breadth

    def getPerimeter(a):
        perimeter = 2*(a.length+a.breadth)
        return perimeter

    def getArea(a):
        area = (a.length*a.breadth)
        return area

l1=int(input("Enter the length of Rect1: "))
b1=int(input("Enter the breadth of Rect1: "))
l2=int(input("Enter the length of Rect2: "))
b2=int(input("Enter the breadth of Rect2: "))

rect1 = Rectangle(l1,b1)
rect2 = Rectangle(l2,b2)

print("Area of Rectangle 1 : ",rect1.getArea())
print("Perimeter of Rectangle 1 : ",rect1.getPerimeter())

print("Area of Rectangle 2 : ",rect2.getArea())
print("Perimeter of Rectangle 2 : ",rect2.getPerimeter())

if(rect1.getArea()>rect2.getArea()):
    print("Rectangle 1 is bigger")
else:
    print("Rectangle 2 is bigger")
