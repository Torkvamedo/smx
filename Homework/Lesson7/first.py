while True:
     a = input('enter word')
     try:
       a = str
     except TypeError:
        print('wrong input')
     else:
        print('Good job')
