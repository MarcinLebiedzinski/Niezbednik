import random

def games_room():
    user_score = 0
    computer_opponent_score = 0
    round = 1
    print("""
    Welcome to my game room! Let's play '2001' Game
    Below are the rules:
    1. The quests always start!
    2. There are two players. You and me.
    3. Each player starts with 0 points.
    4. Each player rolls two cubic dices on his/her round.
    5. The result of each throw is added to the player total number of points.
    6. Starting from the second round:
        - if player rolls a 7, he/she divides his/her number of points by the value, discarding the fractional part
        - if player rolls an 11, he/she multiplies the current number of points by that value 
    7. The goal is to score 2001 points. Who will be first wins!
    
    Are You ready to loose? If so, press Enter.
    """)

    print("If You are ready please press Enter!")
    input()
    while user_score < 2001 or computer_opponent_score < 2001:
        print(f"Round {round}. Press Enter to roll dice.")
        input()
        user_roll_dice1 = random.randint(1, 6)
        user_roll_dice2 = random.randint(1, 6)
        computer_roll_dice1 = random.randint(1, 6)
        computer_roll_dice2 = random.randint(1, 6)
        sum_user_roll_dice = user_roll_dice1 + user_roll_dice2
        sum_computer_roll_dice = computer_roll_dice1 + computer_roll_dice2

        if round == 1 or (round > 1 and sum_user_roll_dice != 7 and sum_user_roll_dice != 11):
            user_score += sum_user_roll_dice
            print(f"""   
            The result of the dice roll:
            Dice nr 1 = {user_roll_dice1}
            Dice nr 2 = {user_roll_dice2}
            The result of dice roll = {sum_user_roll_dice}
            
            Your total score: {user_score}  
            """)

        elif round > 1 and sum_user_roll_dice == 7:
            user_score = int(user_score / 7)
            print(f"""   
            The result of the dice roll:
            Dice nr 1 = {user_roll_dice1}
            Dice nr 2 = {user_roll_dice2}
            The result of dice roll = {sum_user_roll_dice}
            Bad luck! Total score is divided by 7!
            
            Your total score: {user_score}  
            """)
        elif round > 1 and sum_user_roll_dice == 11:
            user_score = user_score * 11
            print(f"""   
            The result of the dice roll:
            Dice nr 1 = {user_roll_dice1}
            Dice nr 2 = {user_roll_dice2}
            The result of dice roll = {sum_user_roll_dice}
            Bonus! Total score is multiplied by 11

            Your total score: {user_score}  
            """)

        if round == 1 or (round > 1 and sum_computer_roll_dice != 7 and sum_computer_roll_dice != 11):
            computer_opponent_score += sum_computer_roll_dice
            print(f"""
            Now It's my turn   
            The result of the dice roll:
            Dice nr 1 = {computer_roll_dice1}
            Dice nr 2 = {computer_roll_dice2}
            The result of dice roll = {sum_computer_roll_dice}

            My total score: {computer_opponent_score}  
            """)

        elif round > 1 and sum_computer_roll_dice == 7:
            computer_opponent_score = int(computer_opponent_score / 7)
            print(f"""
            Now It's my turn   
            The result of the dice roll:
            Dice nr 1 = {computer_roll_dice1}
            Dice nr 2 = {computer_roll_dice2}
            The result of dice roll = {sum_computer_roll_dice}
            Bad luck! Total score is divided by 7!

            My total score: {computer_opponent_score}  
            """)
        elif round > 1 and sum_computer_roll_dice == 11:
            computer_opponent_score = computer_opponent_score * 11
            print(f"""
            Now It's my turn   
            The result of the dice roll:
            Dice nr 1 = {computer_roll_dice1}
            Dice nr 2 = {computer_roll_dice2}
            The result of dice roll = {sum_computer_roll_dice}
            Bonus! Total score is multiplied by 11

            My total score: {computer_opponent_score}  
            """)

        round += 1

if __name__ == '__main__':
    print(games_room())

