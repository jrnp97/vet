import time
from yaspin import yaspin, Spinner

from services.base import ServiceInterface


class Limpieza(ServiceInterface):
    """ Class to represent and handle Limpieza Service """

    @classmethod
    def get_price(cls) -> float:
        return 10.50

    def execute(self) -> None:
        process = [
            ("✨", "Checking"),
            ("💧", "Filling the tub",)
            ("🛁", "Whashing",),
            ("🧴", "Applying the soap"),
            ("🌼", "Applying odor",),
            ("🧼", "Cleaning the body",),
            ("🧽", "Cleaning the head",),
            ("🚿", "Rinsing out",),
            ("💧", "Cleaning extra stuff",),
            ("🛀🏽", "Drying up",),
            ("✨", "Cleaning check"),
        ]
        with yaspin(text="Preparing") as sp:
            for emoji, text in process:
                time.sleep(5)
                sp.spinner = emoji
                sp.text = text
            sp.ok()

