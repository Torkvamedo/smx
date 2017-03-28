bubbles = [1,16,-5,17,88,3,27,123,-145,0]

def puziryok_sort(new_bubbles):
    pink = len(new_bubbles) - 1
    for x in range (0,pink):
        for v in range(0,pink):
            if new_bubbles[v]>new_bubbles[v+1]:
                new_bubbles[v],new_bubbles[v+1] = new_bubbles[v+1],new_bubbles[v]
    return new_bubbles
print(puziryok_sort(bubbles))
