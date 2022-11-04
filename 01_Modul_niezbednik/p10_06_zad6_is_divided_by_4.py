def id_divisible_by_4(number):
    print(f"Liczba {number} jest podzielna przez 4 - {number % 4 == 0}")
    return number % 4 == 0


print("----------------")
id_divisible_by_4(4)
id_divisible_by_4(16)
id_divisible_by_4(15)
print("----------------")