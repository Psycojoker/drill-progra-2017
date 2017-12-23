def f2(dic, x):
    list = []

    for y, z in dic.items():
        if z == x:
            list.append(y)

    list.append(x)

    return list


def f(l1, l2):
    dic = {}
    g = 0

    for x in l1:
        z = 0
        for y in l2:
            if (x % y == 0):
                if y >= z:
                    z = y

        if (z != 0):
            dic[x] = z

            if z >= g:
                g = z

    return f2(dic, g)

l1 = [10, 8, 9, 6, 12]
l2 = [1, 2, 3, 4]
print f(l1, l2)

l1 = [5, 7, 10, 13, 15, 20]
l2 = [1, 2, 5, 10]
print f(l1, l2)

l1 = [1, 10, 14, 20, 24, 30]
l2 = [2, 3, 4, 5]
print f(l1, l2)
