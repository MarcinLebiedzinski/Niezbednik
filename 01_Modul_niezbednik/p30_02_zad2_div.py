def div():
    try:
        number1 = abs(int(float(input("Podaj wartość liczby1: "))))
        number2 = abs(int(float(input("Podaj wartość liczby1: "))))
        print(f"Wynik dzielenia podanych liczb: {number1} i {number2} jest równy ", number1 / number2)
    except ValueError:
        print("Podano niewłaściwe dane!")
    except ZeroDivisionError:
        print("Nie wolno dzielić przez '0'!")


div()



# Inne zadanie z lekcji - sprawdza czy liczby są całkowite i czy nie ma dzielenia przez 0
def divide(a, b):
    try:
        if not (isinstance(a, int) and a > 0) or not (isinstance(b, int) and b > 0):
            print("Podane liczby nie są liczbami naturalnymi!")
        return a / b
    except ZeroDivisionError:
        print("Nie wolno dzielić przez zero!")
    except TypeError:
        print("Wartości nie są liczbami")


print(divide(2, 'a'))