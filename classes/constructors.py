# self variable is a must in creating a constructor by using __init__
# I differentiated class variable and local variable with different names so to not confuse.

# class variables are visible[in scope] and usable across the class.
# local variables are only visbile[in scope] and usable only within that method

class Point:
    def __init__(self, x_localVariable, y_localVariable):
        self.xClasVariable = x_localVariable
        self.yClassVariable = y_localVariable

    def draw(self):
        print("drawing....from ", self.xClasVariable,
              " to ", self.yClassVariable)


# point1 = Point()
point1 = Point(1, 2)
print(point1.yClassVariable, point1.yClassVariable)  # 1 2
point1.draw()  # drawing....from  1  to  2
