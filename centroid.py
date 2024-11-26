def centroid(*args):
    a = max(*args)
    c = len(a)
    List = []
    Values = []
    for i in args :
        e = c-len(i)
        f =  list(i)+[0]*e
        List.append(f)
        Points = zip(*List)
    for i in Points:
         b = sum(i)/len(i)
         Values.append(b)
    print(Values)   
    return Values
centroid((1,2,3,10),(1,2,3,4,5),(1,2,0))


