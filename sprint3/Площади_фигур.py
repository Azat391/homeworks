# Площади фигур 📐
from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self, width,height):
        super().__init__()
        self.width=width
        self.height=height
        # self._area=0
    def area(self):
        return self.width*self.height
class Square:
    def __init__(self,side):
        super().__init__()
        self.side=side
    def area(self):
        return self.side**2
def total_area(shapes):
    result=0
    for i in shapes:
        result+=i.area()
    return result
shapes=[Rectangle(3,4), Square(5), Rectangle(2,6)]
print(total_area(shapes))
print(Square(1).area())
print(total_area(Square([])))