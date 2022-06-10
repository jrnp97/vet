""" module to define all dog logic """
from animals import Animal, AnimalControl


class Cachorro(Animal, AnimalControl):  # Especializaçao
    # Sobreescribi o metodo __init__
    def __init__(self, nome, sobrenome, nome_do_dono, idade, raza, tipo):
        super().__init__(nome, sobrenome, nome_do_dono, idade, raza, "DOMESTICO")

    def __dict__(self):
        return {
            "nome": self.nome,
            "sobrenome": self.sobrenome,
            "nome_do_dono": self.nome_do_dono,
            "idade": self.idade,
            "raza": self.raza,
            "tipo": self.tipo,
        }

    def __repr__(self):
        return f"Cachorro {self.nome}"

    def __str__(self):
        return f"Cachorro {self.nome}"
