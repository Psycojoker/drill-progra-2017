li1 = [20, 24, 8, 6, 10, 32, 15, 3]


def f1(l1):
    pos = 0

    for a in l1:
        if a >= 20:
            x = a
            pos = pos + 1
            l1.remove(a)
            l1.insert(0, x)

    l1.append(pos)

    return l1


def pg(x, ly):
    m = 0

    for a in ly:
        if x % a == 0:
            if a > m:
                m = a

    return m


def end(lis):
    dx = {}
    lx = f1(lis)

    for a in lx:
        if a >= 20:
            loc = []
            x = lis[len(lis) - 1]
            i = x

            while i < len(lis) - 1:
                loc.append(lis[i])
                i = i + 1

            dx[a] = pg(a, loc)

    return dx

print end(li1)
