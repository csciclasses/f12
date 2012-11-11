import random

##Python program

'''
Generic 2-D point
'''
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def display(self):
        return 'x={0}, y={1}'.format(self.x, self.y)

'''
Base shape class
'''         
class Shape:
    def display():
        pass

    def sort_order(self):
        return self.__sort_order

    def __init__(self):
        self.__sort_order = random.Random().randint(0,10)

'''
Shape subclasses
'''
class Circle(Shape):
    def __init__(self, center_point, radius):
        Shape.__init__(self)
        self.radius = radius
        self.center_point = center_point

    def display(self):
        return 'Circle - Sort {0} - Radius {1} center @ {2}'.format(self.sort_order(), self.radius, self.center_point.display())

class Square(Shape):
    def __init__(self, start_point, side_len):
        Shape.__init__(self)
        self.side_len = side_len
        self.start_point = start_point 

    def display(self):
        return 'Square - Sort {0} -Side Length {1} starting @ {2}'.format(self.sort_order(), self.side_len, self.start_point.display())


class Triangle(Shape):
    def __init__(self, vertex_one, vertex_two, vertex_three):
        Shape.__init__(self)
        self.vertex_one = vertex_one
        self.vertex_two = vertex_two
        self.vertex_three = vertex_three

    def display(self):
        return 'Triangle - Sort {0} - Vertices @ {1}, {2} and {3}'.format(self.sort_order(), self.vertex_one.display(), self.vertex_two.display(), self.vertex_three.display())


'''
Main Program and helper functions
'''
def init_shapes_db():
    return [
        Circle(Point(3,3), 5),
        Square(Point(7,4), 4),
        Triangle(Point(4,4), Point(3,3), Point(2,2)),
        Triangle(Point(14,4), Point(33,3), Point(-2,2)),
        Square(Point(0,0), 4),
    ]


#initialize the shapes db
shapes = init_shapes_db()

#sort the shapes
sorted_shapes = sorted(shapes, key=lambda x:x.sort_order())

print   #empty line
print 'Number of Shapes: {0}'.format(len(shapes))
print   #empty line
#display all shapes
for shape in sorted_shapes:
    print shape.display()    
print   #empty line
#display all shapes in sorted order
