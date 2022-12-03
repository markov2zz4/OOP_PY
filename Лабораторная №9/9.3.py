from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

point1 = Point(5, 7)
point2 = Point(-10, 12)

print(point1.x, point1.y)
print(point2.x, point2.y)