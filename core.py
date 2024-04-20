
        pass
    def change_plane(cls):
    @classmethod

        pass
    def change_soi_in(cls):
    @classmethod

        pass
    def change_soi_out(cls):
    @classmethod

        atmosDV =                                    # maybe?

        vel_h = circumference / rotational_period     # 1,600 kilometers per hour = 40,075 km / 24h

        Ek = 1/2 * m * v**2                           # Calculate kinetic energy

        ep = m * g * h                                # m = 1
    def astmos_launch(cls):
    @classmethod

        return Dv
            Dv = Tv - Sv
            Tv = t["u"] * (2 / t["Rp"] - 1 / t["a"])  # Calculate target velocity
            Sv = s["u"] * (2 / s["Rp"] - 1 / s["a"])  # Calculate starting velocity
        else:                                         # Starting SMA lower than target SMA
            Dv = Sv - Tv
            Tv = t["u"] * (2 / t["Ra"] - 1 / t["a"])  # Calculate target velocity
            Sv = s["u"] * (2 / s["Ra"] - 1 / s["a"])  # Calculate starting velocity
        if s["a"] >= t["a"]:                          # Starting SMA higher than target SMA

        t = cls.calculate_target(body_name, target_orbit)
        s = cls.calculate_start(body_name, starting_orbit)
    def calculate_delta(cls, body_name, starting_orbit, target_orbit):
    @classmethod

        return {"u": u, "Ra": Ra, "Rp": Rp, "a": a}
        T = 2 * pi * sqrt(a**3 / u)     # Orbital period
        a = (Ra + Rp) / 2               # Semi-major axis
        Rp = Pe + R                     # Periapsis measured from the center of the body
        Ra = Ap + R                     # Apoapsis measured from the center of the body
        R = body[body_name]["R"]        # Body radius
        u = body[body_name]["GM"] * 100 ** body[body_name]["Ex"]  # Gravitational parameter
        Ap, Pe = target_orbit

        body = get()
    def calculate_target(cls, body_name, target_orbit):
    @classmethod

        return {"u": u, "Ra": Ra, "Rp": Rp, "a": a}
        T = 2 * pi * sqrt(a ** 3 / u)   # Orbital period
        a = (Ra + Rp) / 2               # Semi-major axis
        Rp = Pe + R                     # Periapsis measured from the center of the body
        Ra = Ap + R                     # Apoapsis measured from the center of the body
        R = body[body_name]["R"]        # Body radius
        u = body[body_name]["GM"] * 100 ** body[body_name]["Ex"]  # Gravitational parameter
        Ap, Pe = starting_orbit

        body = get()
    def calculate_start(cls, body_name, starting_orbit):
    @classmethod

        pass
    def run(cls):
    @classmethod
class DeltaVPlanner:


        return Td
        Td = (2 * a * b / h) * (1 / sin(body[body_name]["R"] / b) + (e * body[body_name]["R"] / b))

        h = sqrt(l * u)                     # Specific angular momentum
        u = (body[body_name]["GM"] * 10 ** body[body_name]["Ex"]) / 1000 ** 3   # Gravitational parameter
        l = (2 * (Ra * Rp)) / (Ra + Rp)     # Semi-latus rectum of the orbital ellipse
        e = (Ra - Rp) / (Ra + Rp)           # Eccentricity
        b = sqrt(Ra * Rp)                   # Semi-minor axis
        a = (Ra + Rp) / 2                   # Semi-major axis
        Rp = Pe + R                         # Periapsis measured from the center of the body
        Ra = Ap + R                         # Apoapsis measured from the center of the body
        R = body[body_name]["R"]            # Body radius

        body = get()
    def calculate(cls, body_name, Ap, Pe):
    @classmethod

        Interface.main_menu()
        Interface.dark_side_calc_result(Td)
        Td = cls.calculate(bn, ap, pe)
        bn, ap, pe = Interface.dark_side_calc_input()
    def run(cls):
    @classmethod
class DarkSideCalc:


from utils import get
from cli import Interface

from numpy import cbrt
from math import sqrt, sin, pi
