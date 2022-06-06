"""
Criar um programa para uma veterinaria, com os seguintes features:
    1. Control animais => Cadastro, Actualizaçao, Detalhe, Eliminaçao. [os animais tem dono]
        1.1 Nome, Sobrenome, Nome Dono, Idade, Raça, tipo.
    2. Control donos => Cadastro, Actualizaçao, Detalhe, Eliminaçao. [os donos tem animais]
        2.1 Nome, Sobrenome, Endereço, Idade, Animais.
    3. CRUD de serviços => medicos, tosa.
        3.1 Animal, Data inicio, Data finalizaçao, Valor, Detalhes.

"""
from pprint import pprint

import animals
from animals import Cachorro, Macaco
from services.clean import Limpieza
from services.doctor import Medico
from services.payment import Pago


animales = {
    Cachorro.__name__: [],
    Macaco.__name__: [],
}

registro_servicios = {
    Medico.__name__: [],
    Limpieza.__name__: [],
}


def control_animal() -> None:
    """ Funcion para control animal """ # docstring
    animal_opts = {
        1: {
            "class": Cachorro,
            "option": Cachorro.__name__,
        },
        2: {
            "class": Macaco,
            "option": Macaco.__name__,
        },
        3: {
            "option": "Salir"
        }
    }
    action_opts = {
        1: {
            "method": "cadastrar",
            "option": "Cadastrar",
        },
        2: {
            "method": "actualizar",
            "option": "Actualizar",
        },
        3: {
            "method": "detalhe",
            "option": "Detalhe",
        },
        4: {
            "method": "eliminar",
            "option": "Eliminar",
        },
        5: {
            "method": "display_all",
            "option": "Mostrar todos",
        },
        6: {
            "option": "Salir",
        }
    }

    while True:
        print("*"*10, "CONTROL ANIMAL", "*"*10)
        option, animal_opt = menu_displayer(menu=animal_opts)
        if option == 3:
            return

        selected_action, action_opt = menu_displayer(menu=action_opts)
        if selected_action == 6:
            return

        if not hasattr(animal_opt['class'], action_opt['method']):
            print("Operacao nao esta disponivel no momento")
            continue

        action = getattr(animal_opt['class'], action_opt['method'])
        action()


def servicios_management() -> None:
    """ Funcion para controlar los servicios """
    print("-"*10, "SERVICIOS", "-"*10)
    menu = {
        1: {
            "class": Medico,
            "option": "Atendimiento medico",
        },
        2: {
            "class": Limpieza,
            "option": "Limpieza Animal",
        },
        3: {
            "class": Pago,
            "option": "Pagamento Servicio",
        },
        4: {
            "fnc": lambda: exit(),
            "option": "Salir",
        }
    }
    _, option = menu_displayer(menu=menu)
    option.run(animales=animales, registro=registro_servicios)


main_menu = {
        1: {"option": "Control Animal", "action": control_animal},
        2: {"option": "Servicios", "action": servicios_management},
        3: {"option": "Salir", "action": lambda : exit()}
}
while True:
    print("*"*10, "VETERINARIA", "*"*10)
    _, option = menu_displayer(menu=main_menu)
    option["action"]()


