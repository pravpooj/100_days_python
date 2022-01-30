







print('Wellcome to Pizza place')

Size = input("what size of pizza would you like to order?(S,M,L):")
pep = input("would you like to add Peporoni:(Y,N)?: ")
Cheese = input("Would you like some extra cheez?(Y,N):")

bill = 0

if Size == "S": 
    bill += 15

elif Size == "M":
    bill +=20 
elif Size == "L":
    bill += 25
if pep == "Y":
    if Size == "S":
        bill += 2
    else:
        bill += 3
if Cheese == "Y":
    bill += 1

print(bill)


