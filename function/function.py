def area_of_triangle(b, h):
    area = (1/2) * b * h
    return area

def area_of_rectangle(l,b):
    area = l * b
    return area

shape_type = int(input("What shape is it?." + "\n" + "Enter 1 for Triangle" + "\n" + "Enter 2 for Rectangle" + "\n" + ":"))


if shape_type == 1:
    b = int(input("Enter the based of the triangle: "))
    h = int(input("Enter the height of the Triangle: "))
    print(f"The area of the Triangle is: {area_of_triangle(b, h)}")


elif shape_type == 2:
    l = int(input("Enter the length of the rectangle: "))
    b = int(input("Enter the breadth of the rectangle: "))
    print(f"The area of the Rectangle is: {area_of_rectangle(l, b)}")

else:
    print("You did not select the right option. Please select the right option ( ͡° ͜ʖ ͡°)" + "\n" )
    shape_type = int(input("What shape is it?." + "\n" + "Enter 1 for Triangle" + "\n" + "Enter 2 for Rectangle" + "\n" + ":"))





