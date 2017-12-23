def func1(li1, li2, x, y):
    li3 = []

    for a in li1:
        if (a != x):
            if (a != y):
                li3.append(a)

    for a in li2:
        if ((a != x)or(a != y)):
            li3.append(a)

    return li3


def func2(li1, li2, x, y, n):
    li4 = func1(li1, li2, x, y)

    xx = 0
    li5 = []

    while (xx < n):
        li5.append(li4[xx])
        xx = xx + 1

    return li5

print func2('titi', 'toto', 't', 'o', 3)
print func2('solvay', 'orange', 'o', 'a', 5)
print func2('ULB', 'Universite', 'U', 'L', 6)
print func2('informatique', 'Python', 'P', 'y', 12)
