f = open('C:\\Users\\Aliwka\\Desktop\\ДЗ-курсы\\Homework6\\first.txt', 'r')
w = open('C:\\Users\\Aliwka\\Desktop\\ДЗ-курсы\\Homework6\\second.txt','w')

d = sorted(f.readlines())
w.write(''.join(d))
