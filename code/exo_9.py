import random

liste = ["pipo", "etudiant"]


def M2(x, y):
    a = input("Allez-y: ")

    j = 0
    yy = ''

    for le in x:
        if a == le:
            yy += a
        else:
            yy += y[j]
        j += 1

    print (yy)

    return yy


def M1(x):
    y = ''

    for a in x:
        y += '-'

    print (y)

    tt = 0

    while (tt < 5):
        y = M2(x, y)
        xx = input("Faites une proposition: ")

        if xx == x:
            print("Gagne!!!!!!!!!")
            tt = 5

        else:
            if(tt == 4):
                print("Perdu!!!!!!!!!")

        tt += 1

    vv = input("Une fois encore ?: ")
    return vv


def M():
    re = "oui"

    while (re == "oui"):
        m = liste[random.randint(0, len(liste) - 1)]
        re = M1(m)

M()
