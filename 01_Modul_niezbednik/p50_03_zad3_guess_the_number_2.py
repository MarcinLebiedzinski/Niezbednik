def user_answer():
    while True:
        print("""
        I'm a right? Please type me:
        1 - if the number is too big
        2 - if the number is to small
        3 - if I won
        Your answer: 
        """)
        user_answer = input()
        if user_answer not in ('1', '2', '3'):
            print("Wrong choice! Try again")
            continue
        else:
            return user_answer


def guess():
    min = 0
    max = 1000
    step = 1
    while step <= 10:
        guess_number = int((max - min) / 2) + min
        print(f"My {step} try. I guess: ", guess_number)
        a = user_answer()
        if a == '3':
            print(f"I won!, number of tries = {step}")
            break
        elif a == '1':
            max = guess_number
            step += 1
        elif a == '2':
            min = guess_number
            step += 1
        # print("No of tries more than 10. You are winner!")


print("""
_____________________________________________________________________
Imagine the number from 0 to 1000 and I will guess it in max 10 steps
""")

if __name__ == '__main__':
    guess()
