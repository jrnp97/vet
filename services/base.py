""" Module to define Service Interfaces """
from animals import Animal, TYPES
from veterinaria.utils import menu_displayer, select_instance

class ServiceInterface:

    def __init__(self, _id: int, animal: Animal, data_de_inicio: datatime.datetime, valor: float):
        self.identifier = _id
        self.animal = animal
        self.data_de_inicio = data_de_inicio
        self.valor = valor

    def __str__(self):
        return f"[{self.__class__.__name__.upper()}] {self.identifier} {self.animal} {self.data_de_inicio}"

    @classmethod
    def get_price(cls) -> float:
    	raise NotImplemented

    def execute(self) -> None:
    	raise NotImplemented


    @classmethod
    def run(cls, animales: dict, registro: dict) -> None:
    	if not animales:
    		print("No animals type available")
    		return
    	if cls.__name__ not in registro:
    		print("Invalid registro dict")
    		return

    	print(f"{cls.__name__.upper()}", "-"*10, sep='\n')
    	print("-"*5, " Selecting Animal Type")
    	animal_opts = {
    		idx: {
    			"class": animal_type,
    			"option": animal_type.__name__,
    		}
    		for idx, animal_type in enumerate(TYPES)
    	}
	    _, animal_type = menu_displayer(menu=animal_opts)

	    list_animals = animales.get(animal_type["option"], [])
	    if not list_animals:
	    	print(f"No exists registered animals of type: {animal_type['option']} registered")
	    	return
	    print("-"*5, " Selecting Animal")
	    for idx, animal in enumerate(list_animals):
	    	print(f"{idx}. {animal}")

	    selected_index = select_instance(
	    	object_name=animal_type["option"],
	    	max_value=len(list_animals),
	    )
	    animal = list_animals[selected_index]

	    service = cls(
	    	animal=animal,
	    	data_de_inicio=datetime.datetime.now(),
	    	valor=cls.get_price(),
	    )
	    print("-"*5, " Executando o Servico")
	    service.execute()


