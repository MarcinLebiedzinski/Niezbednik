from random import shuffle

def input_user_number():
    user_list = []
    i = 1
    while len(user_list) < 6:
        try:
            user_number = int(input(f"Please input Your number {i} : "))
        except ValueError:
            print("Its not number!")
            continue
        if user_number < 1 or user_number > 49 or user_number in user_list:
            print("Number should be in range from 1 to 49 and Your numbers can't repeat!")
            continue
        else:
            user_list.append(user_number)
            i += 1

    user_list.sort()
    print("Your numbers: ", user_list)
    print("--------------------------")
    return user_list


def lotto():
    hit_numbers =[]
    print("------------------------------------------")
    print("Hello! This is Lotto Game! Do You want be a millionaire? Try your luck! ")
    print("------------------------------------------")
    user_list = input_user_number()
    print("Let's start the draw! Press enter!")
    input()
    set_of_number = [number for number in range(1, 49)]
    shuffle(set_of_number)
    drawn_numbers = set_of_number[:6]
    drawn_numbers.sort()
    print("Here are the numbers in today's draw", drawn_numbers)
    print("--------------------------")

    for drawn_number in drawn_numbers:
        if drawn_number in user_list:
            hit_numbers.append(drawn_number)

    print(f"Yoy hit {len(hit_numbers)} number correctly. Here's is hitted number {hit_numbers}")


if __name__ == '__main__':
    lotto()
