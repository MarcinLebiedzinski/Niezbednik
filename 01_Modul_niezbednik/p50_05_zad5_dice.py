from random import randint


def throw_dice(combination):

    if not isinstance(combination, str):
        print("Invalid combination. Please input another one")
        return None
    else:
        amount_of_plus = combination.count("+")
        amount_of_d = combination.count("D")

        if amount_of_d != 1 and (amount_of_plus != 0 or amount_of_plus != 1):
            print("Invalid combination. Please input another one")
            return None

    list_of_combination = combination.replace("D", " ").replace("+", " ").split(" ")
    list_of_combination = [i for i in list_of_combination if i != ''] # removing empty elements ''

    if len(list_of_combination) == 3:
        number_of_throw = list_of_combination[0]
        type_of_dice = list_of_combination[1]
        number_to_add = list_of_combination[2]
    elif len(list_of_combination) == 2 and amount_of_plus == 1:
        number_of_throw = 1
        type_of_dice = list_of_combination[0]
        number_to_add = list_of_combination[1]
    elif len(list_of_combination) == 1:
        number_of_throw = 1
        type_of_dice = list_of_combination[0]
        number_to_add = 0
    else:
        number_of_throw = list_of_combination[0]
        type_of_dice = list_of_combination[1]
        number_to_add = 0

    try:
        number_of_throw = int(number_of_throw)
        type_of_dice = int(type_of_dice)
        number_to_add = int(number_to_add)
    except ValueError:
        print("Invalid combination. Please input another one")
        return None

    sum_of_throw = 0
    for i in range(number_of_throw):
        sum_of_throw += randint(1, type_of_dice)
    sum_of_throw += number_to_add

    print("------------------------------------------------")
    print(f"I'm throwing the dice - combination {combination}")
    print(f"Number of throws = {number_of_throw}")
    print(f"Type of dice = D{type_of_dice}")
    print(f"Number to add = {number_to_add}")
    print("------------------------------------------------")
    return sum_of_throw


if __name__ == '__main__':
    # print(throw_dice('2D20+10'))
    # print(throw_dice('2D100'))
    # print(throw_dice('D10+10'))
    # print(throw_dice('210+10'))
    # print(throw_dice('a1D20+1b'))

    print(throw_dice("2D10+10"))
    print(throw_dice("D6"))
    print(throw_dice("2D3"))
    print(throw_dice("D12-1"))
    print(throw_dice("DD34"))
    print(throw_dice("4-3D6"))
