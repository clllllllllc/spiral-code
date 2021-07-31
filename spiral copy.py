import math
import ti_plotlib as plt


class Spiral:
    """Spiral object"""

    def __init__(self, *constants):
        """create values"""
        self.end_value = constants[0]
        self.c = [float(c) for c in constants]
        self.values = []
        self.x = []
        self.y = []

    def n(self, t: float) -> float:
        """calculate n"""
        p1 = math.sqrt((self.c[1] * t))
        p2 = math.ceil((p1 - 1)/2)
        p3 = self.c[2] * p2
        return p3

    @staticmethod
    def z(t: float, n: float) -> float:
        p1 = t - (2 * n - 1) ** 2
        return p1

    def d(self, z: float, n: float) -> float:
        p1 = (self.c[3] * z) % (2 * n)
        p2 = self.c[5] * abs(p1 - self.c[4] * n)
        return p2

    def u1(self, z: float, n: float) -> float:
        p1 = (self.c[6] * z - 1e-6) / (self.c[7] * 2 * n)
        p2 = math.floor(p1)
        p3 = p2 % 2
        return p3

    def u2(self, z: float, n: float) -> float:
        p1 = (self.c[8] * z - 1e-6) / (self.c[9] * 2 * n)
        p2 = math.ceil(p1)
        p3 = p2 % 2
        return p3

    def v1(self, z: float, n: float) -> float:
        p1 = (self.c[10] * z - n) / (4 * n)
        p2 = math.floor(p1) % 2
        return p2

    def v2(self, z: float, n: float) -> float:
        p1 = (self.c[11] * z + n) / (4 * n)
        p2 = math.floor(p1) % 2
        return p2

    def p(self, u1: float, u2: float, v1: float, n: float, d: float) -> float:
        p1 = (0 ** u1) * d + (0 ** u2) * n
        p2 = self.c[12] * p1 * (-1) ** v1
        return p2

    def q(self, u1: float, u2: float, v2: float, n: float, d: float) -> float:
        p1 = (0 ** u2) * d + (0 ** u1) * n
        p2 = self.c[13] * p1 * (-1) ** v2
        return p2

    def get_value(self, t: float):
        n = float(self.n(t))
        z = float(self.z(t, n))
        d = float(self.d(z, n))
        u1 = float(self.u1(z, n))
        u2 = float(self.u2(z, n))
        v1 = float(self.v1(z, n))
        v2 = float(self.v2(z, n))
        p = float(self.p(u1, u2, v1, n, d))
        q = float(self.q(u1, u2, v2, n, d))
        return [p, q]

    def get_spiral(self) -> None:
        for i in range(2, self.end_value + 1):
            self.values.append(self.get_value(float(i)))
        self.x = [v[0] for v in self.values]
        self.y = [v[1] for v in self.values]

    def draw_spiral(self) -> None:
        plt.cls()
        plt.plot(self.x, self.y)
        plt.auto_window(self.x, self.y)
        plt.show_plot()


def main():
    spiral = Spiral(2500, 1, 1, 1, 3.4, 1, 1, 1, 1, 1, 9.6, -0.2, 1.9, 1.1)
    spiral.get_spiral()
    spiral.draw_spiral()


if __name__ == "__main__":
    main()
