# def is_concatenate(word, dictionary):                 задача на конкатенацию
#     if (word == ''):                                  (как на собеседовании)
#         return True
#
#     for i in range (1,len(word)):
#         temp = word[0:i+1]
#         if (temp in dictionary):
#             if is_concatenate(word[i+1:],dictionary):
#                 return True
#
#     return False
#
# print(is_concatenate('aaaaa',['aab','aa','aaa','cdf']))

# --------------------------------------------------------

# a = 10
# def func(b):              глобальная
#     global a
#     a = 30
#     return a+b
#
# print(func(10))

# --------------------------------------------------------

# def f():
#     a = 30
#     def g():      не локальная
#        nonlocal a
#        a = 40
#     g()
#     return a
# print(f())

# ------------------------------------------------------------------

# x = 10        (part_2_second_2.py)
# def f():
#     return x

# def map(f,list):
#     new_list=[]
#     for elem in list:
#         new_list.append(f(elem))
#     return new_list
#
# def funcz(x):
#     return x+2
#
# l = [10,20,30]
# print(map(funcz,l))

# --------------------------------------------------------------


# def map(f,lis):                           задача на reduce / функции высшего порядка
#     return [f(elem) for elem in lis]
#
# def func(x):
#     return x+2
#
# def plus(a,b):
#     return a+b
#
# def reduce(g,init,lis):
#     sum = init
#     for i in lis:
#        sum=g(sum,i)
#     return sum
#
# l = [10,20,30]
# new_l = map(func,l)
# res = reduce(plus,0,new_l)
# print(res)
#----------------------------------------------------------------------
# def func():             декораторы
#     def g(x):
#         return x+10
#
#     return g
#
# res = func()
# print(res(50))

