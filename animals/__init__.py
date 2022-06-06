""" Package initializer """

from veterinaria.utils import solicitacao_dados

DATA = dict(
    nome="Nome",
    sobrenome="Sobrenome",
    nome_do_dono="Nombe do Dono",
    idade="Idade",
    raza="Raza",
    tipo="Tipo",
)


class AnimalControl:

    @classmethod
    def exists_animais(cls):
        return bool(animales[cls.__name__])

    @classmethod
    def cadastrar(cls):
        print("-"*10, "REGISTRO ANIMAL","-"*10)
        dados = solicitacao_dados(datos=DATA)
        animal = cls(**dados)
        print(f"{cls.__name__.capitalize()} CRIADO: {animal}")
        animales[cls.__name__].append(animal)
        return animal

    @classmethod
    def actualizar(cls):
        print("-"*10, "ACTUALIZACION ANIMAL","-"*10)
        if not cls.exists_animais():
            print("Nao é possivel utilizar essa opcao, nao existem animais cadastrados")
            return
        animal_index = select_instance(
            object_name=cls.__name__, 
            max_value=len(animales[cls.__name__])
        )
        animal = animales[cls.__name__][animal_index]
        print(animal, "&"*5)
        dados = solicitacao_dados(datos=DATA)
        for key, value in datos.items():
            setattr(animal, key, value)
        return animal

    @classmethod
    def detalhe(cls):
        print("-"*10, "DETALLE ANIMAL","-"*10)
        if not cls.exists_animais():
            print("Nao é possivel utilizar essa opcao, nao existem animais cadastrados")
            return
        animal_index = select_instance(
            object_name=cls.__name__, 
            max_value=len(animales[cls.__name__])
        )
        animal = animales[cls.__name__][animal_index]
        print(animal)
        return 

    @classmethod
    def eliminar(cls):
        print("-"*10, "ELIMINACION ANIMAL","-"*10)
        if not cls.exists_animais():
            print("Nao é possivel utilizar essa opcao, nao existem animais cadastrados")
            return
        animal_index = select_instance(
            object_name=cls.__name__, 
            max_value=len(animales[cls.__name__])
        )
        confirmation = input("Estas seguro que deseas eliminarlo? [y/n]: ")
        if confirmation == "y":
            animales[cls.__name__].pop(animal_index)
        else:
            print("Eliminacion abortada :)")
        return 

    @classmethod
    def display_all(cls):
        print("ANIMALES")
        pprint(animales[cls.__name__])


# Representaçoes da Vida real
class Animal:

    def __init__(self, nome, sobrenome, nome_do_dono, idade, raza, tipo):
        self.nome = nome
        self.sobrenome = sobrenome
        self.nome_do_dono = nome_do_dono
        self.idade = idade
        self.raza = raza
        self.tipo = tipo

    def __str__(self):
        return f"{self.nome} {self.sobrenome} - {self.tipo}"


from animals.dog import Cachorro
from animals.monkey import Macaco

TYPES = (
    Cachorro,
    Macaco
)