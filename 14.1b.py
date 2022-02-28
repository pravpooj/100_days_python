from calendar import c
import imp
from os import name
import random
from art import hl_logo
from art import vs
from game_data import data
from clearscreen import clrscr

print(hl_logo,"\n")


def format_data(account):
    """Take the account data and formate it"""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"


def check_answer(guess, a_follower, b_follower):
    """Take the user guess and return if they got it right"""
    if a_follower > b_follower:
        return guess == "a"
    else:
        return guess == "b"
     #   if guess =='a':
     #       return True
     #   else:
     #       return False
score = 0
game_on = True
b = random.choice(data)

while game_on:
    a = b
    a_follower = int(a['follower_count'])
    b = random.choice(data)
    b_follower = int(b['follower_count'])
    while a == b:
        b = random.choice(data)

    print(f"Compare A:{format_data(a)}")
    print(vs)
    print(f"Compare B:{format_data(b)}\n")
    guess = input(f"Who has more Insta followers: \n A: {a['name']} \n or \n B: {b['name']} \n ").lower()
    is_correct = check_answer(guess, a_follower,b_follower)
    clrscr()
    print(hl_logo)
    if is_correct:
        score += 1
        print(f"You are right and your current score  is {score}")
    else:
        game_on = False
        print(f"Sorry, losser, that's wrong and final score is {score}")
        

