from services.base import ServiceInterface


class Limpieza(ServiceInterface):
    """ Class to represent and handle Limpieza Service """

    @classmethod
    def get_price(cls) -> float:
        return 10.50

    def execute(self) -> None:
        pass
