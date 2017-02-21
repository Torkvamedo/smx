f = open('C:\\Users\\Aliwka\\Desktop\\ДЗ-курсы\\Homework5\\red.txt','r')
for line in f:
    line
    print(line)
f.close()
l = ['1: строка из файла','2: строка из файла','3: строка из файла','4: строка из файла']
f = open('C:\\Users\\Aliwka\\Desktop\\ДЗ-курсы\\Homework5\\red.txt','w')
for index in l:
    f.write(index + '\n')
    print(index)
f.close()
