def square_area(a, b):
    return a * b


print("----------")
print(square_area(1, 2))
print(square_area(3, 4))
print("----------")

a = float(input("Podaj wartość a: "))
b = float(input("Podaj wartość b: "))
print(f"Pole prostokąta o długości boków a={a} i b={b} wynosi {square_area(a,b)}")
