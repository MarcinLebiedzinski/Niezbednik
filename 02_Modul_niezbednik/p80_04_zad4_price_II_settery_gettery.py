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

    @property
    def netto(self):
        return self.get_netto()

    @property
    def brutto(self):
        return self.get_brutto()

    @property
    def tax(self):
        return self.get_tax()

    @netto.setter
    def netto(self, new_netto):
        self._netto = new_netto
        self._tax = self._netto * 0.23
        self._brutto = self._netto * 1.23

    @brutto.setter
    def brutto(self, new_brutto):
        self._brutto = new_brutto
        self._netto = self._brutto / 1.23
        self._tax = self._netto * 0.23

    @tax.setter
    def tax(self, new_tax):
        self._tax = new_tax
        self._netto = self._tax / 0.23
        self._brutto = self._netto * 1.23


price = Price23Vat(123)

print(price.brutto)
print(price.tax)
print(price.netto)

price.tax = 69

print(price.brutto)
print(price.tax)
print(price.netto)


