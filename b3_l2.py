class Square:
    def __init__(self, side):
        self.side = side
    def cal_area(self):
        return self.side ** 2
    
class Cube :
    def __init__(self, side):
        self.side = side
    def cal_area(self):
        return self.side ** 2 * 6
    def cal_volume(self):
        return self.side ** 3

square = Square(2)
print('Square area:', square.cal_area())

cube = Cube(2)
print('Cube area:', cube.cal_area())
print('Cube volume:', cube.cal_volume())

    