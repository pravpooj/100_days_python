
 import random
 
 
 name = input("Give me everyone's names, seperated by a coma.: ")
 
 name = name.split(", ")
 
 #print(random.choice(name))
 numlist = len(name)
 rendom_name = random.randint(0, numlist -1)
 pay = name[rendom_name]
 
 print(f"{pay} will be paying the bills for Lunch today")



row1 = ["🤡","👿","👺"]
row2 = ["💩","👹","👽"]
row3 = ["😹","🤖","💀"]

map = [row1,row2,row3]





possision = input("Where do you want to put the tresure? ")

#possision = list(possision)
x = int(possision[0]) 
y = int(possision[1])
#x = int(x)-1
#y = int(y)-1

Place = [map[x -1][y -1]] = '🔲'
#print(map[0])
#print(map[1])
#print(map[2])

print(f"{map[0]}\n{map[1]}\n{map[2]}")
