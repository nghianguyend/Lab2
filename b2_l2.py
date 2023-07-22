class MathList:
    def __init__(self, num):
        self.data = num

    def __str__(self):
        return str(self.num)

    def __add__(self, num):
        return MathList([x + num for x in self.num])

    def __sub__(self, num):
        return MathList([x - num for x in self.num])

m_list = MathList([1, 2, 3, 4, 5])
print(m_list)         

m_list += 2
print(m_list)   