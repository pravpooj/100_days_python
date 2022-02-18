

def prime_finder(num):
    is_prime = True
    for i in range(2,num):
        if num%i == 0:
            is_prime = False
    if is_prime:
        print("It's a Prime number")
    else:
        print("It' not prime number")




prime_finder(73)