import time
from yaspin import yaspin
from services.base import ServiceInterface


class Medico(ServiceInterface):
    """ Class to represent and handle Doctor Service """

    @classmethod
    def get_price(cls) -> float:
        return 10.50

    def execute(self) -> None:
        process = [
            "💉: Extract Blood",
            "🩸: Analyzing",
            "💊: Apply vitamins",
            "🩹: Applying curative",
            "🩺: Checking body",
            "🚪: Go to room",
            "🛏: Lie down waiting results",
        ]
        with yaspin(text="In progress") as sp:
            for msg in process:
                time.sleep(5)
                sp.write(msg)
            sp.text = "Executed successfully"
            sp.ok("✔")


