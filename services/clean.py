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
            "โจ: Checking",
            "๐ง: Filling the tub",
            "๐: Whashing",
            "๐งด: Applying the soap",
            "๐ผ: Applying odor",
            "๐งผ: Cleaning the body",
            "๐งฝ: Cleaning the head",
            "๐ฟ: Rinsing out",
            "๐ง: Cleaning extra stuff",
            "๐: Drying up",
            "โจ: Cleaning check",
        ]
        with yaspin(text="In progress") as sp:
            for msg in process:
                time.sleep(5)
                sp.write(msg)
            sp.text = "Executed successfully"
            sp.ok("โ")

