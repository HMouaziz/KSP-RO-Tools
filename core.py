from math import sqrt, sin

from cli import Interface
from utils import get


class DarkSideCalc:
    @classmethod
    def run(cls):
        bn, ap, pe = Interface.dark_side_calc_input()
        Td = cls.calculate(bn, ap, pe)
        Interface.dark_side_calc_result(Td)
        Interface.main_menu()

    @classmethod
    def calculate(cls, body_name, Ap, Pe):
        body = get()

        Ra = Ap + body[body_name]["R"]
        Rp = Pe + body[body_name]["R"]
        a = (Ra + Rp) / 2
        b = sqrt(Ra * Rp)
        e = (Ra - Rp) / (Ra + Rp)
        l = (2 * (Ra * Rp)) / (Ra + Rp)
        u = (body[body_name]["GM"] * 10 ** body[body_name]["Ex"]) / 1000 ** 3
        h = sqrt(l * u)

        Td = (2 * a * b / h) * (1 / sin(body[body_name]["R"] / b) + (e * body[body_name]["R"] / b))
        return Td
