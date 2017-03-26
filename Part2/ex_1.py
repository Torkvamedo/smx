def func(tup):
    return tup[-1]


def print_words(filename):
    f = open("C:\\Users\\Aliwka\\Desktop\\ДЗ-курсы\\Part2\\ex_1.txt",'r')
    whole_content = (f.read()).lower()
    print (whole_content)
    list_content = whole_content.split()
    dict = {}
    for one_word in list_content:
        dict[one_word] = 0
    for one_word in list_content:
        dict[one_word] += 1
    print (dict.items())
    print (sorted(dict.items(),key=func))



