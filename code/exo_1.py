def func(x):
    a = 0
    for i in x:
        a = a + 1
    return a


def func2(x):
    s = 0
    it = 0
    a = func(x)
    r = 0

    while it < a - 1:
        s = s + x[it]
        it = it + 1

    if (s % 2 == 0) and (x[a - 1] == 1):
        r = 1
    elif (s % 2 == 1) and (x[a - 1] == 0):
        r = 1
    else:
        r = 0

    return r

list = []
list2 = []

list.append((1, 0))
list.append((1, 1, 0))
list.append((1, 0, 0, 1, 1))
list.append((1, 0, 0, 0, 1))
list.append((0, 0, 1))
list.append((0, 0, 1, 0))

for x in list:
    list2.append(func2(x))

print list2
