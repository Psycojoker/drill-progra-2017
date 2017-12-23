def f1(k1):
    s=0
    m=0

    for i in k1:
        if type(i) is int:
            s=s+i
            m=m+1

    return s/m

def f2(k2):
    a2=100
    li=[]

    for i in k2:
        ij = f1(i)
        if ij <=5:
            if ij < a2:
                li.insert(0,i[0])
                a2=ij
            else:
                li.append(i[0])

    return li

liste=[("Jean",1,2,3),("Marc",8,10),("Eric",3,6,10,5),("Pierre",1,4,5),("Fred",1,1,1)]
print f2(liste)
