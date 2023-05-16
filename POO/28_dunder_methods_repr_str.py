class Ponto:
    def __init__(self, x, y, z='String'):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f'{self.x}, {self.y}'
    
    def __repr__(self):
        class_name = type(self).__name__
        return f'{class_name} (x={self.x!r}, y={self.y!r}, z={self.z!r})'
    

p1 = Ponto(1, 2)
p2 = Ponto(978, 345)

print(p1)
print(p2)
print(repr(p1))
print(f'{p2!r}')
