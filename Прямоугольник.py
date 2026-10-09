#Прямоугольник 📐
class Rectangle:
    def __init__(self, width,height):
        self.width=width
        self.height=height
    def area(self):
        self.area=self.width*self.height
        return self.area
    def perimetr(self):
        self.perimetr=2*(self.width+self.height)
        return self.perimetr
rectangle = Rectangle(3, 4)

print(rectangle.width)
print(rectangle.height)
print(rectangle.area())
print(rectangle.perimetr())