def validate_pesel(pesel):
    list_of_factor = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    pesel_list = [int(number) for number in pesel]
    if len(pesel_list) != 11:
        return False

    check_digit = pesel_list.pop(10)
    products = []

    for num1, num2 in zip(list_of_factor, pesel_list):
        products.append(num1 * num2)

    if not (10 - (sum(products)) % 10) == check_digit:
        return False
    else:
        return True


print(validate_pesel('82061600331'))

# print(list_of_factor)
# print(pesel_list)
# print(check_digit)
# print(products)
# print(sum(products))
# print(sum(products) % 10)
