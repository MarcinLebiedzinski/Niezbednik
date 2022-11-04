class Price:
    def __init__(self, value):
        self.value = round(float(value), 2)

    @classmethod
    def from_usd(cls, value_usd):
        value_in_pln = value_usd * 3.8
        return Price(value_in_pln)

    @classmethod
    def from_eur(cls, value_eur):
        value_in_pln = value_eur * 4.5
        return Price(value_in_pln)

    def __str__(self):
        return f"{self.value}zł"


price1 = Price(25.666)
print(price1.value)
print(price1)

price2 = Price.from_usd(25)
print(price2.value)
print(price2)

price3 = Price.from_eur(80)
print(price3.value)
print(price3)
