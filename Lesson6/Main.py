from Task1 import Rectangle, Square, Circle

rect_1 = Rectangle(3, 4)
rect_2 = Rectangle(12, 6)

print(rect_1.get_area())
print(rect_2.get_area())

square_1 = Square(5)
square_2 = Square(7)

circle_1 = Circle(2)

print(circle_1.circle_area())
print(rect_1.get_area())
print(rect_2.get_area())

figures = [rect_1, rect_2, square_1, square_2]
for figure in figures:
    if isinstance(figure, Square):
        print((figure.get_area_square()))
    else:
        print(figure.get_area())