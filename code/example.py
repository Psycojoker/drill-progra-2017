def find(li1, li2):
    lx = []
    lx2 = []
    y = z1 = z2 = xx = yy = zz2 = 0

    for a1 in li2:
        y = y + 1

    z1 = 1

    for a2 in li1:
        z2 = 1

        for a3 in li2:
            if a2 == a3 and z2 == zz2 + 1:
                lx.append(z1)
                xx = xx + 1
                zz2 = z2
                z2 = z2 + 1

                if (xx == y):
                    lx2.append(lx[0])
                    lx = []
                    xx = 0
                    zz2 = 0

            z2 = z2 + 1
        z1 = z1 + 1
    return lx2

print find('gta', 'gt')
print find('aagtaaaa', 'aaa')
print find('gtcgtcgtc', 'gtc')
print find('gtaaacgtcgaataac', 'gtc')
