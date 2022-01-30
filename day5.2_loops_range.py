num = 0
for even in range(0,101, 2):
     num += even   
print(num)

from ast import Pass


for num in range(0, 101):
    if num % 3 ==0 and num % 5 ==0 :
        print("FizzBUZZ")
    elif num % 3 == 0:
        print('Fizz')
    elif num % 5 == 0:
        print("Buzz") 

    else:
        print(num)

    

