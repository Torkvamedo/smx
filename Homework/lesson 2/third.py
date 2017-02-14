a='Cruel World'
print(a[a.rfind(' ')+1:]+a[a.find(' ')]+a[:a.find(' ')])


# Придумал второе решение, но не получается изменить список на строку
# a = 'cruel world'
# a = a.split()
# b = a.reverse()
# c = str(b)
# print (c)
