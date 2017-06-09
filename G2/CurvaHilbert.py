import turtle, math


class CurvaHilbert(turtle.Pen):
    def curva(self, size, level, parity):
        if level == 0:
            return
        self.left(parity * 90)
        self.curva(size, level - 1, -parity)
        self.forward(size)
        self.right(parity * 90)
        self.curva(size, level - 1, parity)
        self.forward(size)
        self.curva(size, level - 1, parity)
        self.right(parity * 90)
        self.forward(size)
        self.curva(size, level - 1, -parity)
        self.left(parity * 90)

    def fractalgon(self, n, rad, lev, dir):
        edge = 2 * rad * math.sin(math.pi / n)
        self.pu()
        self.fd(rad)
        self.pd()
        self.rt(180 - (90 * (n - 2) / n))
        for i in range(n):
            self.fractal(edge, lev, dir)
            self.rt(360 / n)
        self.lt(180 - (90 * (n - 2) / n))
        self.pu()
        self.bk(rad)
        self.pd()

    def fractal(self, dist, depth, dir):
        if depth < 1:
            self.fd(dist)
            return
        self.fractal(dist / 3, depth - 1, dir)
        self.lt(60 * dir)
        self.fractal(dist / 3, depth - 1, dir)
        self.rt(120 * dir)
        self.fractal(dist / 3, depth - 1, dir)
        self.lt(60 * dir)
        self.fractal(dist / 3, depth - 1, dir)


def main():
    ch = CurvaHilbert()
    ch.reset()
    ch.speed(1)  # Velocidade da curva.  0 = Rápido, 1 = Lento
    ch.ht()
    ch.getscreen().tracer(1, 0)
    ch.pu()
    size = 12
    ch.setpos(-17 * size, -15 * size)
    ch.pd()
    ch.begin_fill()
    ch.fd(size)
    ch.curva(size, 5, 1)
    input("Pressione ENTER para finalizar")


if __name__ == '__main__':
    main()
