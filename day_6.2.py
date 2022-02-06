#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json

def turn_right():
    for i in range(0,3):
        turn_left()

def bhag_robo():
    if front_is_clear() and wall_on_right():
        move()
    elif front_is_clear() or not front_is_clear() and not wall_on_right():
        turn_right()
        move()
        turn_right()
        move()
    
    elif not front_is_clear():
        turn_left()


while not at_goal():
        bhag_robo()
        