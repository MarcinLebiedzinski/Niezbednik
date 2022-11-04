class User:
    def __init__(self, mail, name, surname):
        self.mail = mail
        self.name = name
        self.surname = surname

class VIPUser(User): # Klasa VIP dziedziczy po klasie User

    def __init__(self, mail, name, surname, card_number):
        super().__inir__(name=name, mail=mail, surname=surname) #wywołujemy metodę init z klasy nadrzędnej
        if self._check_card_number(card_number): # przyowłanie metody statycznej
            self._card_number = card_number
        else:
            self._card_number = None

    @staticmethod
    def _check_card_number(new_number):
        return card_number > 999 and card_number % 2 == 0


    # @staticmethod - Metody statyczne  - dekorator pozwala wywołać metodę bez instancji, nie przekazuje żadnej wartości
    # w pierwszym argumencie - ani self ani cls,
    # Możemy ją stosować w innych metodach wewnętrznych klasy np. w __init__
    # np. self._chceck_card_number lub cls._check_card_number (dla @classmethod)
    # Można się do niej dostać z zewnątrz

    # tutaj metody użyliśmy do sprawdzenia poprawności nr karty w metodzie init podczas tworzenia instancji

