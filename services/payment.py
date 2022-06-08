"""Module to define payment logic"""
from services.doctor import Medico
from services.clean import Limpieza
from veterinaria.utils import menu_displayer, select_instance
from yaspin import yaspin


class Pago:

    @classmethod
    def run(cls, animales: dict, registro: dict) -> None:
        print(f"{cls.__name__.upper()}", "-" * 10, sep='\n')
        print("-" * 5, " Selecting Service Type")
        service_opts = {
            idx: {
                "class": service_type,
                "option": service_type.__name__,
            }
            for idx, service_type in enumerate([Limpieza, Medico])
        }
        _, service_type = menu_displayer(menu=service_opts)

        list_services = registro.get(service_type["option"], [])
        if not list_services:
            print(f"No exists registered services of type: {service_type['option']}")
            return
        print("-" * 5, " Selecting Service")
        for service in list_services:
            print(f"{service.identifier}. {service}")

        selected_index = select_instance(
            object_name=service_type["option"],
            max_value=len(list_services),
        )
        service = list(filter(lambda svs: svs.identifier == selected_index, list_services))
        if not service:
            print("Service was not found.")
            return
        service = service[0]
        if service.is_paid:
            print("O Servico esta pago")
            return

        with yaspin("Processando pagamento") as sp:
            service.pay()
            time.sleep(10)
            sp.text = "Pagamento Existoso!"
            sp.ok("✔")

