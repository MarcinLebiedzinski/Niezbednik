from random import randint

computer_number = randint(1, 100)

while True:
    try:
        user_number = input("Guess the number: ")

        if computer_number == int(user_number):
            print("You win!")
            break
        elif computer_number > int(user_number):
            print("Too small!")
        elif computer_number < int(user_number):
            print("Too big!")
    except ValueError:
        print("It's not number")





# from random import randint
#
# computer_number = randint(1, 100)
#
#
#
# def check_number(user_number):
#     try:
#         checked_number = int(user_number)
#         return checked_number
#     except ValueError:
#         print("It's not number!")
#         return False
#
#
# while True:
#     user_number = input("Guess the number in range from 1 to 100: ")
#
#     if check_number == True:
#
#         if computer_number == int(user_number):
#             print("You win!")
#             break
#         elif computer_number > int(user_number):
#             print("Too small!")
#         elif computer_number < int(user_number):
#             print("Too big!")
#
#     else:









