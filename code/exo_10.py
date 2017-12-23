import random

dico = {}


def test(x):
    x1 = random.randint(x, 10 * x)
    y1 = random.randint(x, 10 * x)
    z1 = random.randint(1, 4)
    r1 = 0

    if (z1 == 1):
        print (str(x1) + ' + ' + str(y1))
        r1 = x1 + y1
    elif (z1 == 2):
        print (str(x1) + ' - ' + str(y1))
        r1 = x1 - y1
    elif (z1 == 3):
        print (str(x1) + ' x ' + str(y1))
        r1 = x1 * y1
    else:
        print (str(x1) + ' / ' + str(y1))
        r1 = x1 / y1

    rx = input('Allez-y: ')

    if (float(rx) == r1):
        return 1
    else:
        return 0


def fi():
    na = input('nom: ')

    for x, y in dico.items():
        if x == na:
            return na

    dico[na] = 1

    return na


def tot():
    nn = True

    while (nn):
        na = fi()
        jj = 0
        xx = 0

        while (xx < 20):
            jj += test(dico[na])
            xx += 1

        if (jj > 10):
            dico[na] *= 10

        nn = input('On continue? False=nom, True=oui: ')

tot()
