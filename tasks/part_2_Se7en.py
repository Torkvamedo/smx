#--------Gof (порождающие паттерны) Builder-----------------------------------------------------------------------------
#
# class Building:
#     def make_basement(self,basement):
#         pass
#     def make_walls(self,walls):
#         pass
#     def make_roof(self,roof):
#         pass
#
# class Sky_scriber(Building):
#     def __init__(self):
#         self.basement = None
#         self.walls = None
#         self.roof = None
#
#     def make_basement(self, basement):
#         self.basement = basement
#
#     def make_walls(self, walls):
#         self.walls = walls
#
#     def make_roof(self,roof):
#         self.roof = roof
#
# class Cottage(Building):
#     def __init__(self):
#         self.basement = None
#         self.walls = None
#         self.roof = None
#
#     def make_basement(self, basement):
#         self.basement = basement
#
#     def make_walls(self, walls):
#         self.walls = walls
#
#     def make_roof(self, roof):
#         self.roof = roof
#
# class Foreman:
#     def __init__(self,builder):
#         self.builder = builder
#
#     def build(self):
#         self.builder.build_basement()
#         self.builder.build_walls()
#         self.builder.build_roof()
#
#
# class Builder:
#     def __init__(self):
#         self.building = None
#     def get_building(self):
#         return self.building
#
#     def build_basement(self):
#         pass
#
#     def build_walls(self):
#         pass
#
#     def build_roof(self):
#         pass
#
#
# class Sky_scriber_builder(Builder):
#     def __init__(self):
#         Builder.__init__(self)
#         self.building = Sky_scriber()
#
#     def build_basement(self):
#             self.building.make_basement("basement")
#
#     def build_walls(self):
#         self.building.make_walls("walls")
#
#     def build_roof(self):
#         self.building.make_roof("roof")
#
#
# class Cottage_builder(Builder):
#     def __init__(self):
#         Builder.__init__(self)
#         self.building = Sky_scriber()
#
#     def build_basement(self):
#         self.building.make_basement("basement")
#
#     def build_walls(self):
#         self.building.make_walls("walls")
#
#     def build_roof(self):
#         self.building.make_roof("roof")
#
# def main():
#     cottage_builder = Cottage_builder()
#     foreman = Foreman(cottage_builder)
#     foreman.build()
#     cottage = cottage_builder.get_building()
#
# main()
# ----------------------------------------------------------------------------------------------------------------------
#
# ----------(Анти) Паттерн Singleton------------------------------------------------------------------------------------

# class Singleton():
#     instance = None
#     def __new__(cls, *args, **kwargs):
#         if Singleton.instance == None:
#             Singleton.instance = object.__new__(cls)
#         return Singleton.instance
#     def __init__(self,a):
#         self.a = a
#
# a1 = Singleton(10)
# a2 = Singleton(39)
# print(a1.a)
# print(a2.a)
# print(a1==a2)
# ----------------------------------------------------------------------------------------------------------------------
#
# -------Flyweight приспособленец---------------------------------------------------------------------------------------
#
# class Character_flyweight():
#     def __init__(self,character):
#         self.character = character
#
# class Factory():
#     def __init__(self):
#         self.map = {}
#     def instance_character(self,char):
#         if self.map.get(char)!= None:
#             return self.map.get(char)
#         else:
#             c = Character_flyweight(char)
#             self.map[char] = c
#             return c
# factory = Factory()
#
# def convert_to_list(word):
#     lis = []
#     for char in word:
#         lis.append(factory.instance_character(char))
#     return lis
#
# lis_word = convert_to_list("abbaaa").
# print(lis_word)
# ----------------------------------------------------------------------------------------------------------------------
#----------------Proxy pattern-------реализация кеша--------------------------------------------------------------------
# class Operation:
#     def operation(self,a,b):
#         return a + b
#
# class Proxy_operation():
#     def __init__(self):
#         self.operation = Operation
#         self.cache = []
#
#     def operation(self,a,b):
#         for tup in self.cache:
#             if tup[0] == a and tup[1] == b:
#                 return tup[2]
#
#
#         res = self.operation.operation(a,b)
#         self.cache.append((a,b,res))
#         return res
# ----------------------------------------------------------------------------------------------------------------------
# =========работа с Super()===================================

# class A:
#     def __init__(self,a):
#      self.a = a
#
# class B:
#     def __init__(self,b):
#        A.__init__(self,a)
#         self.b = b
#  ------------------------
#
# class B(A):
#     def __init__(self,a,b):
#         super(B,self).__init__(a)
#         self.b = b
# pb = B(10,20)
# print(pb)

