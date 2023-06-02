import datetime
import sys

from InquirerPy import inquirer
from InquirerPy.base import Choice
from InquirerPy.validator import EmptyInputValidator

from utils import get


class Interface:

    @classmethod
    def main_menu(cls):
        from core import DarkSideCalc
        """Main menu function"""
        message = ""
        mode = inquirer.select(
            message=message,
            choices=[
                Choice(value=1, name="Run"),
                Choice(value=None, name="Exit"),
            ],
            default=1,
            qmark="-",
            amark="-"
        ).execute()
        if mode == 1:
            DarkSideCalc.run()
        elif mode is None:
            print("Exiting...")
            sys.exit(1)

    @classmethod
    def dark_side_calc_input(cls):
        """ UI for DarkSideCalc
            - Loads data
            - gets body name from user
            - gets Ap and Pe from user
            - returns input values
        """
        body = get()
        b_name = inquirer.fuzzy(
            message="Select SOI:",
            choices=[
                "Mercury",
                "Venus",
                "Earth",
                "Moon",
                "Mars",
                "Phobos",
                "Deimos",
                "Vesta",
                "Ceres",
                "Jupiter",
                "Io",
                "Europa",
                "Ganymede",
                "Callisto",
                "Saturn",
                "Mimas",
                "Tethys",
                "Dione",
                "Rhea",
                "Titan",
                "Iapetus",
                "Uranus",
                "Miranda",
                "Ariel",
                "Umbriel",
                "Titania",
                "Oberon",
                "Neptune",
                "Triton",
                "Pluto",
                "Charon"
            ],
            default=None,
        ).execute()

        body_name = b_name.lower()

        pe = inquirer.number(
            message="Enter Periapsis(in Km):",
            min_allowed=body[body_name]["MinAlt"],
            max_allowed=body[body_name]["Soi"],
            validate=EmptyInputValidator(),
            default=None,
            replace_mode=True
        ).execute()
        pe = int(pe)
        ap = inquirer.number(
            message="Enter Apoapsis(in Km):",
            min_allowed=pe,
            max_allowed=body[body_name]["Soi"],
            validate=EmptyInputValidator(),
            default=None,
            replace_mode=True
        ).execute()
        ap = int(ap)

        return body_name, pe, ap

    @classmethod
    def dark_side_calc_result(cls, result):
        print(f"\nTime Spent in darkness in 1 orbit: {str(datetime.timedelta(seconds=result))}")

