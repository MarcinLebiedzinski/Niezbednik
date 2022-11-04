from random import randint


def roll(number_of_dices, dice_type=6, mod_number=0):
    sum_of_throw = 0
    score = 0
    allowed_dices = [3, 4, 6, 8, 10, 12, 100]

    if dice_type in allowed_dices:
        for i in range(1, number_of_dices + 1):
            dice_roll_score = randint(1, dice_type)
            print(f"Throw {i} - {dice_roll_score}")
            sum_of_throw += dice_roll_score
            score = sum_of_throw + mod_number
        print(f"Total sum of dices rolls: {sum_of_throw}, Score: {score}")
        return score
    else:
        raise Exception("No such dice!")


print(roll(2, 10, 20))
print("--------------")
print(roll(3, 6, -3))
