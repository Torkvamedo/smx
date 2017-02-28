data = [set(open(i).read().split()) for i in ('C:\\Users\\Aliwka\\Desktop\\ДЗ-курсы\\Homework6\\first.txt', 'C:\\Users\\Aliwka\\Desktop\\ДЗ-курсы\\Homework6\\second.txt')]
diff = data[0].difference(data[1])

if diff:
    print(diff, 'слова которые есть в первом файле, но нет во втором')
    print(data[1],data[0],'слова из обоих файлов')


