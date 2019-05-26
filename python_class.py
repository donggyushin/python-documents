class Rectangle:
    count = 0   # class variable

    # initializer
    def __init__(self, width, height):
        self.width = width
        self.height = height
        Rectangle.count += 1
    # method

    def calcArea(self):
        area = self.width * self.height
        return area

    # private method
    def __internalRun(self):
        print('This is private method')

    # static method
    @staticmethod
    def isSquare(rectWidth, rectHeight):
        return rectHeight == rectWidth

    # class method
    @classmethod
    def printCount(cls):
        print(cls.count)


# test
square = Rectangle.isSquare(5, 5)
print(square)       # True

rect1 = Rectangle(5, 5)
rect2 = Rectangle(2, 5)
rect1.printCount()  # 2
rect2.printCount()  # 2
print('rect2\' area: ', rect2.calcArea())  # 10
print('rect1.width = ', rect1.width)      # 5
