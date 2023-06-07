from math import sqrt, sin, pi
from numpy import cbrt

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

        R = body[body_name]["R"]            # Body radius
        Ra = Ap + R                         # Apoapsis measured from the center of the body
        Rp = Pe + R                         # Periapsis measured from the center of the body
        a = (Ra + Rp) / 2                   # Semi-major axis
        b = sqrt(Ra * Rp)                   # Semi-minor axis
        e = (Ra - Rp) / (Ra + Rp)           # Eccentricity
        l = (2 * (Ra * Rp)) / (Ra + Rp)     # Semi-latus rectum of the orbital ellipse
        u = (body[body_name]["GM"] * 10 ** body[body_name]["Ex"]) / 1000 ** 3   # Gravitational parameter
        h = sqrt(l * u)                     # Specific angular momentum

        Td = (2 * a * b / h) * (1 / sin(body[body_name]["R"] / b) + (e * body[body_name]["R"] / b))
        return Td


class DeltaVPlanner:
    @classmethod
    def run(cls):
        pass

    @classmethod
    def calculate_start(cls, body_name, starting_orbit):
        body = get()

        Ap, Pe = starting_orbit
        u = body[body_name]["GM"] * 100 ** body[body_name]["Ex"]  # Gravitational parameter
        R = body[body_name]["R"]        # Body radius
        Ra = Ap + R                     # Apoapsis measured from the center of the body
        Rp = Pe + R                     # Periapsis measured from the center of the body
        a = (Ra + Rp) / 2               # Semi-major axis
        T = 2 * pi * sqrt(a ** 3 / u)   # Orbital period
        return {"u": u, "Ra": Ra, "Rp": Rp, "a": a}

    @classmethod
    def calculate_target(cls, body_name, target_orbit):
        body = get()

        Ap, Pe = target_orbit
        u = body[body_name]["GM"] * 100 ** body[body_name]["Ex"]  # Gravitational parameter
        R = body[body_name]["R"]        # Body radius
        Ra = Ap + R                     # Apoapsis measured from the center of the body
        Rp = Pe + R                     # Periapsis measured from the center of the body
        a = (Ra + Rp) / 2               # Semi-major axis
        T = 2 * pi * sqrt(a**3 / u)     # Orbital period
        return {"u": u, "Ra": Ra, "Rp": Rp, "a": a}

    @classmethod
    def calculate_delta(cls, body_name, starting_orbit, target_orbit):
        s = cls.calculate_start(body_name, starting_orbit)
        t = cls.calculate_target(body_name, target_orbit)
        if s["a"] >= t["a"]:
            Sv = s["u"] * (2 / s["Ra"] - 1 / s["a"])
            Tv = t["u"] * (2 / t["Ra"] - 1 / t["a"])
            Dv = Sv - Tv
        else:
            Sv = s["u"] * (2 / s["Rp"] - 1 / s["a"])
            Tv = t["u"] * (2 / t["Rp"] - 1 / t["a"])
            Dv = Tv - Sv
        return Dv



