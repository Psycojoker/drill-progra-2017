class Les:

    def __init__(self):
        self.ns = {}
        self.no = str(input("quoi ? "))

    def int(self):
        self.x = int(input("Combien ? "))
        i = 0
        nn = ""

        while (i < self.x):
            nn = str(input("qui ? "))
            self.ns[nn] = int(input("Combien ? "))
            i += 1

    def give(self):
        self.et = []
        ny = 0
        self.my = 0

        for x, y in self.ns.items():
            if y < 7:
                self.et.append(x)
            else:
                ny += 1
                self.my += y

        self.my /= ny

c1 = {}
c2 = {}
x = int(input("Combien ? "))
i = 0

while i < x:
    l = Les()

    l.int()
    l.give()

    c1[l.no] = l.my
    c2[l.no] = l.et

    i += 1

print(c1, c2)
