from calendar import c
import imp
from os import name
import random
from art import hl_logo
from art import vs
from game_data import data

print(hl_logo)



a = random.choice(data)
a_follower = int(a['follower_count'])

b = random.choice(data)
b_follower = int(b['follower_count'])


print(f"Compare A {a['name']}, a {a['description']} and from {a['country']}")
print(vs)
print(f"Compare B {b['name']}, a {b['description']} and from {b['country']}")

game_on = True
while game_on:
    def game():

        global a
        global b
        global game_on
        x = 0
        score = 0
        player = input(f"Who has more Insta followers A# {a['name']} or B# {b['name']} ?").capitalize()
        if player == 'A':
            x = b_follower
            player = a_follower
        elif player == 'B':
            x = a_follower
            player = b_follower
        
        if player > x :
            score += 1
            b = a
            b = random.choice(data)
            print(f"your score is {score}")
        else:
            game_on = False

    game()