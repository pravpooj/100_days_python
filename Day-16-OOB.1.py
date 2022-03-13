import turtle
#Imported Module
#timmy = turtle.Turtle()
#timmy.shape("turtle")
#timmy.color("coral")
#timmy.forward(200)
#timmy.right(200)
#timmy.forward(200)
#print(timmy)
##Object , Module, class
#myscreen = turtle.Screen()
#
##or you cam wrtie this way
##from turtle import Screen, turtles, Screen
#
#
#print(myscreen.canvheight)
#
#myscreen.exitonclick()

from  prettytable import PrettyTable


table = PrettyTable()
table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"])
table.add_column("Type",["Elcetric","Water","Fire"])
print(table)



