import re
result1 = re.findall(r'\b[a]\w+', 'ABCxyz is bsdcdsa acbba foooof zooom')
result2 = re.findall(r'\b[b]\w+', 'ABCxyz bs asdcdsa acbba foooof zooom')
result3 = re.findall(r'\b[c]\w+', 'BCxyz s asdcdsa cbba foooof zooom')
f = open(r'C:\Users\Aliwka\Desktop\ДЗ-курсы\Homework5\blue.txt','w')
f.writelines(result1 )
f.writelines(result2 )
f.writelines(result3 )
print (result1,result2,result3)
f.close()

 
