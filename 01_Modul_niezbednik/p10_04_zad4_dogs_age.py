def dogs_age(age):
    if (age > 0) and (age <=2):
        return age * 10.5
    elif (age > 2):
        return 2 * 10.5 + (age - 2) * 4
    else:
        print("Podano nieprawidłową wartość!")
        return


print('---------------')
print(dogs_age(1))
print(dogs_age(1.5))
print(dogs_age(2))
print(dogs_age(3))
print(dogs_age(5))
print('---------------')

age = float(input("Podaj wiek wg ludzkiego biegu czasu: "))
print(f"Dla ludzkiego biegu czasu równego {age} wiek psi wynosi {dogs_age(age)}")

