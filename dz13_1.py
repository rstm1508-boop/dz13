import math

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"


v1 = Vector2D(3, 4)
v2 = Vector2D(1, -2)

result_add = v1 + v2
print(result_add)

result_sub = v1 - v2
print(result_sub)

length_v1 = v1.length()
print(length_v1)

print(v1)