class Product:
    id = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price
        Product.id += 1
        self.id = Product.id


class ShoppingCart:
    def __init__(self):
        self.products = {}
        self.quantities = {}

    def add_product(self, product):
        if product.id not in self.products:
            self.products[product.id] = product
            self.quantities[product.id] = 1
        else:
            self.products[product.id] = product
            self.quantities[product.id] += 1

    def remove_product(self, product):
        self.products.pop(product.id)
        self.quantities.pop(product.id)

    def change_product_quantity(self, product, new_quantity):
        if product.id in self.products and new_quantity > 0:
            self.quantities[product.id] = new_quantity
        elif product.id in self.products and new_quantity == 0:
            self.products.pop(product.id)
        elif product.id in self.products and new_quantity < 0:
            raise ValueError("Invalid value of quantity!")
        else:
            pass

    def get_receipt(self):
        receipt_print = ""
        cart_sum = 0
        for i in self.products:
            rc_name = self.products[i].name
            rc_amount = self.quantities[i]
            if rc_amount >= 3:
                rc_price = round(self.products[i].price * 0.7, 2)
            else:
                rc_price = self.products[i].price
            total = rc_amount * rc_price
            cart_sum += total
            receipt_print += f"{rc_name} - amount: {rc_amount}, price: {round(rc_price, 2)}, total: {round(total, 2)}\n"
        receipt_print += f"{round(cart_sum, 2)}\n"
        return receipt_print


bread = Product('Bread', 2.70)
ham = Product('Ham', 8.40)
cheese = Product('Cheese', 4.40)
chive = Product('Chive', 1.50)
pepper = Product('Pepper', 2.35)

print(bread.id)
print(pepper.id)
print(pepper.name)
print(pepper.price)

cart = ShoppingCart()
print(cart.products)
print(cart.quantities)
print(cart.get_receipt())

cart.add_product(bread)
cart.add_product(bread)
cart.add_product(bread)
cart.add_product(pepper)
cart.add_product(chive)
cart.change_product_quantity(pepper, 3)
print(cart.products)
print(cart.quantities)

cart.remove_product(bread)
print(cart.get_receipt())
