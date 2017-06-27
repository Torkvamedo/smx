#-- Пирамидальная сортировка

# s = [14,32,8,11,112,7,33,5,6,34,6,45,43,56]
# def heapsort(s):
#     sl = len(s)
#
#     def swap(pi, ci):
#         if s[pi] < s[ci]:
#             s[pi], s[ci] = s[ci], s[pi]
#
#     def sift(pi, unsorted):
#         i_gt = lambda a, b: a if s[a] > s[b] else b
#         while pi*2+2 < unsorted:
#             gtci = i_gt(pi*2+1, pi*2+2)
#             swap(pi, gtci)
#             pi = gtci
#     for i in range ((sl//2)-1, -1, -1):
#         sift(i, sl)
#     for i in range(sl-1, 0, -1):
#         swap(i, 0)
#         sift(0, i)
#
# print(s)
# heapsort(s)
# print(s)

# ---------------------------------------------------------------------------------

#------------ ООП ----------------------


# --- создание простого класса
# class point:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
# def main():
#     p = point(3,4)
#     print(p.x)
#     print(p.__dict__['x'])
#     print(p.y)
#     print(p.__dict__)
#     p1 = point(5,6)
# main()
#-----------------------------------------------------------------------
#


# --- нестатический метод (нестатические поля)
# class point():
#     def f(self):
#         self.x = 500
#
# def main():
#
#     p = point()
#     p.x = 100
#     print(p.x)
#     print(p.__dict__)
#     p1 = point()
#     p1.f()
#     print(p1.x)
#     point.f(p1)

# main()

#----------------------------------------------


class A:
    static_field = 100
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.static_field = 400
    def f(self):
        return self.x +self.y

# p = A(10,20)
# print(p.__dict__)
print(A.__dict__)
print(A.static_field)
p = A(30,40)
print(p.static_field)


