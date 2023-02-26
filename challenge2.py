'''Create a function (it is important that it is only one) that is able 
to calculate and return the area of a polygon.
- The function will receive by parameter only ONE polygon at a time.
- The supported polygons will be Triangle, Square and Rectangle.
- It prints the calculation of the area of one polygon of each type.'''

def calculate_area():
    answer = input('Do you want to calculate the area of a triangle, rectangle or square?: ').lower()
    base = int(input('What is the base?: '))
    height = int(input('What is the height?: '))
    if answer == 'triangle':
        polygon_area = (base * height) / 2
    else:
        polygon_area = base * height

    print(f"The area of {answer} is: {polygon_area}")

calculate_area()


