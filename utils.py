"""Module defining function utils of the program"""

# annotations
def select_instance(object_name: str, max_value: int) -> int:
    """ Function to request a valid user data"""
    result = None
    while result is None or 0 < result < max_value:
        result = int(input(f"Selecciona el {object_name} [0-{max_value-1}]: "))
    return result


def solicitacao_dados(datos: dict) -> dict:
    """
    Function to request user data
    args:
    	datos: A dict with the below structure:
    	{
    		<dato-key>: <display-name>
    	}
    """
    info = {}
    for key, value in datos.items():
        dado = input(f"Por favor diga o valor de {value}: ")
        info[key] = dado
    return info


def menu_displayer(menu: dict) -> tuple:
    """ # docstring
    Function to display and request menu actions
    args:
        menu: A dict with the below structure:
            { 
                <menu_option: int>: {
                    "option": <option to display: str>
                },
                ...
            }
    """
    for key, value in menu.items():
        print(f"{key}. {value['option']}")
    action  = None
    while action is None or action not in menu.keys():
        action = int(input("Seleccione la opcion a realizar: "))
    return action, menu[action]
