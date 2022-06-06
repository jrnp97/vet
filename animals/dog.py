""" module to define all dog logic """
from animals import Animal, AnimalControl


class Cachorro(Animal, AnimalControl):  # Especializaçao
    # Sobreescribi o metodo __init__
    def __init__(self, nome, sobrenome, nome_do_dono, idade, raza, tipo):
        super().__init__(nome, sobrenome, nome_do_dono, idade, raza, "DOMESTICO")
