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




    # Getter - zwraca na zewnątrz parametr ukryty. Gdyby nie było parapetru ukrytego byłaby to zwykła metoda
    @property
    def card_number(self):
        return self._card_number

    # Setter - Pozwala na zmianę parametru na zewnątrz
    @card_number.setter
    def card_number(self, card_number):
        self._card_number = card_number if self._check_card_number(card_number) else None # tu przywołano static method

