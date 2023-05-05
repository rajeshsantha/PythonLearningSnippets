# self variable is a must in creating a constructor by using __init__

class Point:
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
