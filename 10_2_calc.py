from art import calc
from clearscreen import clrscr

print(calc)



def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2

operation = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


n1 = int(input("What's the First number:? \n"))
#operater = input("Pick an Operator:(+,-,*,/)\n")

for symbol in operation:
    print(symbol)
operater = input("Pick an Operator:\n")
n2 = int(input("What's the next number:? \n"))
clrscr()
calculation_fun = operation[operater]
answer = calculation_fun(n1,n2)

print(f"{n1}{operater}{n2} = {answer}")