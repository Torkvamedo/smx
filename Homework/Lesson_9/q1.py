def front_back(a, b):
    print (a, b)
    a_lol = int((len(a)+1)/2)
    b_lol = int((len(b)+1)/2)
    print (a[:a_lol] + b[:b_lol] + a[a_lol:] +b[b_lol:])
    print ("\n")
