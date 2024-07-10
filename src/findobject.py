import pointtopoint

a =4
b =5
c = [6,7,8]

d = "Hi"
"Hello"

def area(x):
    return x **2

print(area(3))



class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


point1 = Point(1,2)
point2 = Point(3,4)

print(type(point2))

p2p = pointtopoint.PointToPoint("p2p")
print(type(p2p))
