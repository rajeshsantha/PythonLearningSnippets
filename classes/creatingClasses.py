# Upper case to begin with , with no underscores in middle
class Point:
    def draw(self):
        print("drawing....")


point1 = Point()
print(type(point1))
# False : not an object of int, so false. its an object of class Point
print(isinstance(point1, int))
point1.draw()  # drawing....
