from os import system, name
from time import sleep

def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


import random
import hangman_words
from hangman_art import stages,logo
#from replit import clear




#from hangman_art import logo

print(logo)


word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(hangman_words.word_list)
word_lenth = len(chosen_word)
print(f"Chosen word is {chosen_word}")

display = []
life = 6

for i in range(word_lenth):
#for i in chosen_word:
    display += "_"
  
end_of_game = False

while not end_of_game:

    guess = input("Guess a Letter:").lower()
    clear()

    for position in range(word_lenth):
        letter = chosen_word[position]
        #print(f"Current possion:{position} \n Current Letter: {letter} \n Gussed Letter {guess}")
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        life -= 1
        print(stages[life])
    
    print(display)


    if "_" not in display:
        end_of_game = True
        print("You win")
    elif life == 0 :
        print("you lose")
        end_of_game = True




