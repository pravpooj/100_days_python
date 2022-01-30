from ast import Pass
import random
 
 

rock = "👊"
paper = "🤚"
scissor = "✌"


mylist = [rock, paper, scissor]
#print(mylist)

comp_select = random.randint(0,2)
print(mylist[comp_select])

choice = int(input("Select one of this : (0 for Rock, 1 for Paper and 2 for secissor: "))
print(mylist[choice])

if comp_select == choice:
    print("Game Draw, Play again")

elif comp_select == 0 and choice == 1:
    print("you win")

elif comp_select == 0 and choice == 2:
    print("you lose")


elif comp_select == 1 and choice == 0 :
    print("you lose")

elif comp_select == 1 and choice == 2:
    print("you win")

elif comp_select == 2 and choice == 1:
    print("you lose")

elif comp_select == 2 and choice == 0 :
    print("you win")


else:
    print('If you want to play select only 0 or 1 or 2')

