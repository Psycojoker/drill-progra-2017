def func(a):
    dic = {}
    dedans = False
    c = 1

    for x in a:
        for y, z in dic.items():
            if (x == y):
                dic[y] = dic[y] + 1
                dedans = True

        if (not dedans):
            dic[x] = c
        dedans = False

    return dic


def change(m):
    dic = func(m)
    n = m

    for x in m:
        for y, z in dic.items():
            if (x == y and z == 2):
                n = n.replace(y, 'z')

    return n

print change("solvay")
print change("pipo")
print change("maman")
print change("java")
