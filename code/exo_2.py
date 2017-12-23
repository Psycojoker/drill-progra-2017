def func(l1,l2):
    a=0
    for i in l1:
        for j in l2:
            if i==j:
                a=a+1
    return a

def func2(l3):
    a=0

    for i in l3:
        a=a+1

    b=0
    res=l3[0]
    a=a-1
    i=0

    while i<a:
        c = func(l3[i],l3[a])
        if (c > b):
            b=c
            res=l3[i]
        i=i+1
    return res

print func2(["AGV073","AGH987","HIJ073","HGV073"])
print func2(["AVH900","GVH988","GVH965","GGG988","GRH966"])
print func2(["DDA011","VDD012","CDA010"])
