class Rectangle :
    def __init__(self, height, width) :
        self.width = width
        self.height = height
    def __str__(self):
        return f"Rectangle object with height = {self.height} and width = {self.width}"

rect = Rectangle(2, 1)
print(rect)
