class Price23Vat:
    def __init__(self, brutto):
        self._brutto = brutto
        self._netto = brutto / 1.23
        self._tax = self._netto * 0.23

    def get_netto(self):
        return self._netto

    def get_brutto(self):
        return self._brutto

    def get_tax(self):
        return self._tax

    def set_netto(self, value):
        self._netto = value
        self._tax = self._netto * 0.23
        self._brutto = self._netto * 1.23

    def set_brutto(self, value):
        self._brutto = value
        self._netto = self._brutto / 1.23
        self._tax = self._netto * 0.23

    def set_tax(self, value):
        self._tax = value
        self._netto = self._tax / 0.23
        self._brutto = self._netto * 1.23

ob1 = Price23Vat(1230)
print(ob1.get_netto())
print(ob1.get_tax())
print(ob1.get_brutto())
ob1.set_netto(2000)
print(ob1.get_tax())
print(ob1.get_brutto())
ob1.set_brutto(3690)
print(ob1.get_tax())
print(ob1.get_netto())
ob1.set_tax(23)
print(ob1.get_netto())
print(ob1.get_brutto())
