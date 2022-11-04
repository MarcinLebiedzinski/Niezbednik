import random

# Funkcja import (Return a random integer N such that a <= N <= b) Również 1 i 20
number = random.randint(1, 20)
print(number)

# Znak nowej liniii
print("I will end with new additional line\n")
print("\nI will start from new additional line")

# Atrybut usunięcia nowej linii i wstawienia str w cudzysłowiu
print("This is first line", end="")
print("This is second line")

print("This is first line", end="gygyu")
print("This is second line")

# Długość stringa
length_of_string = len('Length of string')
print(length_of_string)

# Długość listy
length_of_list = len(['a', 'be', 'ce', 'de'])
print(length_of_list)

# --------------------------- SŁOWNIK ---------------------------

# Utworzenie słownika
dict = {}
size = 8
for i in range(size):
    dict[f"key{i}"] = f"value{i}"
print(dict)

# Iterowanie po słowniku
for key in dict:
    print(key, dict[key])

for key in dict.keys():
    print(key)

for value in dict.values():
    print(value)

for key, value in dict.items():
    print(key, value)

# Usuwanie wartości za pomocą metody pop - wyświetli błąd jeśli nie istnieje klucz
dict.pop("key7")
print(dict)

# sprawdzenie czy jakiś klucz istnieje w słowniku
if "key1" in dict.keys():
    print("Znaleziono")
else:
    print("Nie znaleziono")

# sprawdzenie czy jakaś wartość istnieje w słowniku
if "value1" in dict.values():
    print("Znaleziono")
else:
    print("Nie znaleziono")


# --------------------------- LISTA ---------------------------

# Wyświetlanie list i tupli
my_list = (2, 4 ,8, 16, 32, 64, 128)
print("\nWycinki:")
print(my_list[0:3]) # Pierwsza cyfra oznacza indeks pierwszego elmentu wycinka, druga cyfra oznacza ostatni element ale bez niego (otwarte domknięcie) - ilość elementów
print(my_list[3:5])
print(my_list[0:6])
print(my_list[0:9]) # Pomimo, że ideks nie istnieje nie wygeneruje to błędu, wycinek zakończy sie na końcu krotki
print(my_list[-4:-2]) # można operować na elementach od końca
print(my_list[0:7:2]) #ostatnia cyfra to skok kolekcji czyli w tym przypadku wyświetla co drugie element
print("\n")
print(my_list[0:]) # jeśli drugi argument jest pusty wtyświetlamy kolekcję do samego końca
print(my_list[:4]) # jeśli pierwszy argumrent jest pusty wtyświetlamy kolekcję od samego początku
print(my_list[:]) # Wyświetlenie całej listy
print("\n")
print(my_list[0::2]) # jeśli drugi argument jest pusty wtyświetlamy kolekcję do samego końca (co drugi element)
print(my_list[:4:2]) # jeśli pierwszy argumrent jest pusty wtyświetlamy kolekcję od samego początku (co drugi element)
print("\n")
print(my_list[7:0:-1]) # jeśli wartość skoku będzie -1 to wyświetlimy kolekcję w odwrotnie posortowanej kolejności (elementy wyświetlane od końca)

# Suma listy
list_to_sum = [1, 3, 5, 6, 9, 12]
print(sum(list_to_sum))

# --------------------------- MODUŁ DATETIME ---------------------------

from datetime import datetime, timedelta
def tomorrow():
    return datetime.now() + timedelta(days=1)

print(tomorrow())

# --------------------------- Exceptions ---------------------------

def phone(number, list):
    if number in list:
        return number
    else:
        raise Exception('Nie ma takiego numeru!')


def divide(a, b):
    try:
        if not (isinstance(a, int) and a > 0) or not (isinstance(b, int) and b > 0):
            print("Podane liczby nie są liczbami naturalnymi!")
        return a / b
    except ZeroDivisionError:
        print("Nie wolno dzielić przez zero!")
    except TypeError:
        print("Wartości nie są liczbami")