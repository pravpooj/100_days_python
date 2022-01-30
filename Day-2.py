

#num_char = str(len(input("What's your name?")))

#print(num_char)


#val = (input('Trype the two digit number'))
#print((int(val[0]) + int(val[1])))

hight = float(input("what's your hight in m: "))
weight = int(input("what's your weight in kg: "))

BMI=18
#BMI = (weight//hight**2)

if BMI < 18.5:
    print('You are underweight')
elif BMI > 18.5 and BMI < 25:
    print('Normal Weight')
elif BMI > 25 and BMI < 30:
    print('Over Weight')
elif BMI > 30 and BMI < 35:
    print('Normal Weight')
else:
    print('Clinically Obese')
print(BMI)



