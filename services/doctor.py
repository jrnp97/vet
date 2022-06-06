from services.base import ServiceInterface


class Doctor(ServiceInterface):
    """ Class to represent and handle Doctor Service """

    @classmethod
    def get_price(cls) -> float:
        return 10.50

    def execute(self) -> None:
        pass
