stop = ".,'"


def stopW(word):
    l = word

    for char in stop:
        l = l.replace(char, "")

    return l


def computeBOW(fileName):
    W = {}

    for line in open(fileName):
        for word in line.lower().split():
            word = stopW(word)
            if len(word) > 2:
                if word not in W:
                    W[word] = 0
                W[word] = W[word] + 1

    return W


def PS(fn1, fn2):
    W1 = computeBOW(fn1)
    W2 = computeBOW(fn2)
    res = 0

    for x in W1:
        for y in W2:
            if (x == y):
                res = res + W1[x] * W2[y]
                break

    return res


def select(filename, filelist):
    min = 0

    for f in filelist:
        dist = PS(filename, f)
        if dist > min:
            sel = f
            min = dist

    return sel
