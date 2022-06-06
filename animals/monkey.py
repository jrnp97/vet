""" module to define all monkey logic """
from animals import Animal, AnimalControl


class Macaco(Animal, AnimalControl):
    def __init__(self, nome, sobrenome, nome_do_dono, idade, raza, tipo):
        super().__init__(nome, sobrenome, nome_do_dono, idade, raza, "SALVAJE")
