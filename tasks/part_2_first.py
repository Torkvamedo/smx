# def func(a,b,c): простая функция
#     return a+b+c
#
# res = func(10,20,30)
# print(res)

# -------------------------------------------------------------------

# def func(*a): (a = массив, неопределённое колличество аргументов)
#     res = 0
#     for i in a:
#         res+=i
#         return res
# res=func(10,20)
# print(res)

# --------------------------------------------------------------------

# def myfuncк(**b):      фуннкция со словарём
#     print(b["b"])
#
# myfunc(a = 10,b = 3ейск-----------------------------------------------

# def fact(n):              Рекурсия (посчитать n-факториал)
#     if(n>0):
#         return  fact(n-1)*n
#     else:
#         return 1
# res = fact(3)
# print(res)

# --------------------------------------------------------------------

# Задача Ханойские диски(башни) (рекурсивный алгоритм)
# def hanoy(n,a,b,c):
#     if(n>0):
#         hanoy(n-1,a,c,b)
#         print('disk '+ str(n)+' take from '+a+' to '+c)
#         hanoy(n-1,b,a,c)
#
# hanoy(3,'a','b','c')

# --------------------------------------------------------------------
# 3адача поиск оазисов на карте (алгоритм на графах, теория в глубину)
def area(map,i,j):
    map[i][j] = 2
    if (j-1>=0 and map[i][j-1] == 1):
        area (map,i,j-1)
    if (j+1<len(map) and map[i][j+1] == 1):
        area (map,i,j+1)
    if (i-1>=0 and map[i-1][j]==1):
        area(map,i-1,j)
    if (i+1<len(map) and map[i+1][j]==1):
        area(map,i+1,j)


def fields(map):
    count = 0
    for i in range(0,len(map)):
        for j in range (0,len(map)):
            if (map[i][j]==1):
                count+=1
                area(map,i,j)
    return count

map = [[1,1,0,0,0,],
       [1,0,0,1,1],
       [0,0,0,0,0],
       [1,1,0,0,0],
       [0,0,0,0,1]]
count=fields(map)
print(count)