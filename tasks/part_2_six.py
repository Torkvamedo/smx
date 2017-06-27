# -----------------game  Крестики нолики (uml diagram)---------------------------------
# class game():
#     def __init__(self, player1, player2):
#         self.player1 = player1
#         self.player2 = player2
#
#     def start_game(self):
#         while True:
#             if not self.player1.is_free_cell():
#                 print("draw")
#                 break
#             self.player1.step()
#             if self.player1.is_winner():
#                 print("Player1 is winner!! Godlike ")
#                 break
#             if not self.player2.is_free_cell():
#                 print("Draw ")
#                 break
#             self.player2.step()
#             if self.player2.is_winner():
#                     print("Player2 is Winner !! Rampage")
#                     break
#
#
# class player():
#     def __init__(self, field: object, mark: object) -> object:
#         self.field = field
#         self.mark = mark
#
#     def is_free_cell(self):
#         return self.field.is_free_cell()
#
#     def step(self):
#         pass
#
#
#     def is_winner(self):
#         return self.field.is_line(self.mark)
#
# class human(player):
#     def __init__(self,field,mark):
#         player.__init__(self,field,mark)
#
#     def step(self):
#         x = int(input())
#         y = int(input())
#         self.field.set_mark(x,y,self.mark)
#         self.field.show()
#
#
# class bot(player):
#     def __init__(self,field,mark):
#         player.__init__(self,field,mark)
#
#     def step(self):
#
#         x,y = self.field.free_cell()
#
#         self.field.set_mark(x, y, self.mark)
#         self.field.show()
#
#
# class field():
#     def __init__(self):
#         self.cells = []
#         for i in range(0,3):
#             temmp = []
#             for g in range (0,3):
#                 temmp.append(cell())
#             self.cells.append(temmp)
#
#
#     def is_free_cell(self):
#         for i in range (0,3):
#            for g in range(0,3):
#                if self.cells[i] [g].status == "-":
#                  return True
#
#         return False
#
#     def is_line(self, mark):
#          for i in range(0,3):
#
#              if self.cells[i][0].status  == mark and self.cells[i][1].status == mark \
#                  and self.cells[i][2].status == mark:
#                  return True
#
#          for g in range(0,3):
#              if self.cells[0][g].status == mark and self.cells[1][g].status == mark \
#                  and self.cells[2][g].status == mark:
#                  return  True
#
#              if self.cells[0][0].status == mark and self.cells[1][1].status == mark \
#                   and self.cells[2][2].status == mark:
#                       return  True
#
#              if self.cells[0][2].status == mark and self.cells[1][1].status == mark \
#                      and self.cells[2][0].status == mark:
#                          return False
#
#     def set_mark(self,x,y,mark):
#         self.cells[x][y].status = mark
#
#
#     def show(self):
#          for i in range(0,3):
#              for g in range(0,3):
#                  print(self.cells[i][g].status, end=" ")
#              print()
#          print("--------------------")
#     def free_cell(self):
#         for i in range(0, 3):
#             for g in range(0, 3):
#                 if self.cells[i][g].status == "-":
#                     return (i,g)
#
# class cell():
#     def __init__(self):
#         self.status = "-"
#
#
# def main():
#     field1 = field()
#     player1 = human(field1,"x")
#     player2 = bot(field1, "0")
#     game1 = game(player1,player2)
#     game1.start_game()
#
# main()
#-------------------------------------------------------------------------
#----------------Морской бой( World of Warships )---реализовать дома------

# множественные наследования
#
# class Quadrangle():
#     def __init__(self,line1,line2,line3,angle1,angle2):
#         self.line1 = line1
#         self.line2 = line2
#         self.line3 = line3
#         self.angle1 = angle1
#         self.angle2 = angle2
#
# class Paralellogramm(Quadrangle):
#     def __init__(self,line1,line2,angle):
#         Quadrangle.__init__(self,line1,line2,line1,angle,180 - angle1)
#
# class Rectangle(Paralellogramm):
#     def __init__(self,line1,line2):
#         Paralellogramm.__init__(self,line1,line2, 90)
#
# class Romb(Paralellogramm):
#     def __init__(self,line,angle):
#         Paralellogramm.__init__(self,line,line,angle)
# class Squadron(Romb,Rectangle):
#     def __init__(self,line):
#         Rectangle.__init__(self,line,line)
#         Romb.__init__(self,line,90)

# ------------------------------------------
# class A:
#     def __init__(self,a):
#         self.a = a
# class B:
#     def __init__(self,b):
#         self.b = b
#
# class C(A,B):
#     def __init__(self,a,b):
#         A.__init__(self,a)
#         B.__init__(self,b)
#
#
# def main():
#
#     c = C(10,20)
#
#     print(c.a,c.b)
#     print(C.__dict__)
#
#
# main()
