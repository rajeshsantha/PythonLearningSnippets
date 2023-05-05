# instance variables are specific to instance object.
# point1 xInstanceVariable means 1, but point2 xInstanceVariable means 3
# local variables are only visbile[in scope] and usable only within that method and garbage collected as soon as the method execution completes.

# class variable are defined within scope of class, and the value will be same for all the objects and it will be shared

class Point:
    default_color = "red"  # class variable

    def __init__(self, x_localVariable, y_localVariable):
        self.xInstanceVariable = x_localVariable
        self.yInstanceVariable = y_localVariable

    def draw(self):
        print("drawing....from ", self.xInstanceVariable,
              " to ", self.yInstanceVariable)


# point1 = Point()
point1 = Point(1, 2)
print(point1.xInstanceVariable, point1.yInstanceVariable)  # 1 2
point1.draw()  # drawing....from  1  to  2
print(point1.default_color)  # red


point2 = Point(3, 4)
print(point2.xInstanceVariable, point1.yInstanceVariable)  # 3 4
point2.draw()  # drawing....from  3  to  4
print(point2.default_color)  # red
