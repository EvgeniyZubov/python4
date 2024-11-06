import math

class Point:
    def __init__(self, name, x, y):
        self.name = name
        self.x = float(x)
        self.y = float(y)

    def find_lenght(self, other):
        return math.sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2)

    def add_cords(self):
        self.y = self.y + 43
        return self.y

def task():
     point_list = [
        Point("A", float(input("Enter x for A: ")), float(input("Enter y for A: "))),
        Point("B", float(input("Enter x for B: ")), float(input("Enter y for B: "))),
        Point("C", float(input("Enter x for C: ")), float(input("Enter y for C: "))),
        Point("D", float(input("Enter x for D: ")), float(input("Enter y for D: ")))
        ]

     for point in point_list:
          print(point.name,": (", point.x,";" ,point.y, ") ")


     distance = point_list[0].find_lenght(point_list[3])
     print(f"Відстань між точками {point_list[0].name} та {point_list[3].name}: {distance}")

     print(f"Точка {point_list[1].name} з координатами: ({point_list[1].x};{point_list[1].y}) була пересунута вгору на 43")
     point_list[1].add_cords()
     print(f"Зараз координати точки {point_list[1].name} дорівнюють:({point_list[1].x};{point_list[1].y})")




