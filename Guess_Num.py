
import random
from clearscreen import clrscr

print("Welcome to the Number Guessing Game!")
deficulty = input("Choose a difficulty, Type 'EASY','HARD'\n").lower()
guess = 0
number = list(range(101))
answer = int(random.choice(number))
print(f"Computer number is {answer}")
game = True
while game:
    def game_on(answer):
        global guess
        #print(f" Guess count {guess}")
        global game
        if deficulty == 'easy':
            guess += 1
            print(f"You have {11 - guess} attempts left")
        elif deficulty == 'hard':
            guess += 1
            print(f"You have {6 - guess} attempts left ")

        user_gess= int(input("Please Guess the winning number between '0' to '100':\n"))
        if user_gess < answer:
            print(f"Your guessed number {user_gess} too low, Please try again")
        elif user_gess > answer:
            print(f"Your gussed number {user_gess} is too High, Please try again")
        elif user_gess == answer:
            print("You are the winner, now close the laptop and take break")
            game = False
            
        if deficulty == 'easy' and guess == 9:
            game = False
            print("you lose")

        if deficulty == 'hard' and guess == 4:
            game = False
            print("Losser.. losser")
        

    game_on(answer)