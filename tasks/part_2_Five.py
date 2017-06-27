# расчёт стоимости грузовика с кофе

# class coffee:
#     def __init__(self, type, price):
#         self.type = type
#         self.price = price
#
# class box:
#     def __init__(self, volume,coffee):
#         self.volume = volume
#         self.coffee = coffee
#
# class lorry:
#     def __init__(self):
#         self.boxes = []
#     def add_box(self,box):
#         self.boxes.append(box)
#     def total(self):
#         sum = 0
#         for box in self.boxes:
#             sum += box.volume * box.coffee.price
#         return sum
#
# def main():
#     coffee_arabica = coffee('aravica', 200)
#     coffee_rabusta = coffee('rabusta', 130)
#     box1 = box(40,coffee_arabica)
#     box2 = box(50,coffee_rabusta)
#     box3 = box(10,coffee_arabica)
#     box4 = box(90, coffee_rabusta)
#
#     Lorry = lorry()
#     Lorry.add_box(box1)
#     Lorry.add_box(box2)
#     Lorry.add_box(box3)
#     Lorry.add_box(box4)
#
#     print(Lorry.total())
# main()

#---------------------------------------------------------

#  статический метод (статические поля)
# class A:
#     fields = 10
#     def __init__(self,a):
#         self.a = a
#
#         def f (self):
#             return self.a
#
#         @staticmethod
#         def g():
#             return A.fields

#----------------------------------------------------------

#  наследование
#
# import math
# class point:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#     def distance(self, other):
#         return math.sqrt((self.x - other.x)**2) + math.sqrt((self.y - other.y)**2)
#
# class circle(point):
#     def __init__(self,x,y,radius):
#         point.__init__(self,x,y)
#         self.radius = radius
#
#     def square(self):
#         return 3.14 * self.radius ** 2
#
#
# def main():
#
# Circle = circle(11,27,99)
# print(Circle.radius, Circle.x, Circle.y)
# print(Circle.__dict__)
# print(Circle.square())
#
# Circle2 = circle(5,6,90)
# print(Circle2.distance(Circle))

# main()

#------------------------------------------------------

# полиморфизм

# import math
# class Point:
#      def __init__(self,x,y):
#         self.x = x
#         self.y = y
#
# def distance(point1, point2):
#     return math.sqrt((point1.x - point2.x)**2) + math.sqrt((point1.y - point2.y)**2)
#
# class Circle(Point):
#     def __init__(self, x, y, radius):
#         Point.__init__(self, x, y)
#         self.radius = radius
#     def square(self):
#         return 3.14 * self.radius ** 2
#
# def main():
#     p1 = Point(10,20)
#     p2 = Point(20,40)
#     d = distance(p1,p2)
#     c1 = Circle(30,40,100)
#     c2 = Circle(15,25,80)
#     d1 = distance(c1,c2)
#     print(d1)
#
# main()

# ----------------------------------------------------------------------------------------

#  полиморфизм (фопрос понимания ООП, задача с собеседования)
#
# class A:
#     def __init__(self):
#         self.f()
#     def f(self):
#         print('A')
# class B(A):
#     def __init__(self):
#         A.__init__(self)
#
#     def f(self):
#         print('B')
#
# def main():
#      b = B()
#
# main()


#-------------------------------------------------------------------------------------------



