# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

total_hight = 0
lenth = 0

#This is how sum function works
for hight in student_heights:
    total_hight = total_hight + hight
#print(total_hight)

#this is how len function works
for le in student_heights:
    lenth = lenth + 1
#print(lenth)

avarage = total_hight / lenth

print(f"Avarage hight of the student is {round(avarage)}")


#   +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

highest_score = 0

for score in student_scores:
    if score > highest_score:
        highest_score = score
print(f"Higest score in the class is {highest_score}")
