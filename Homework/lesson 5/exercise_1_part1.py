f = open(r'C:\Users\Aliwka\Desktop\ДЗ-курсы\Homework5\yellow.txt')
lines = f.readlines()
print(lines)
f.close()
lines[0] = "1: строка из файла \n"
lines[1] = "2: строка из файла \n"
lines[2] = "3: строка из файла \n"
lines[3] = "4: строка из файла \n"
f = open(r'C:\Users\Aliwka\Desktop\ДЗ-курсы\Homework5\yellow2.txt','w')
f.writelines(lines)
print(lines)
f.close()




