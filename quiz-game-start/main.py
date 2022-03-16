
from question_model import Question
from quiz_brain import quiz_brain
import requests
import json

url = "https://opentdb.com/api.php?amount=20&category=9&difficulty=medium&type=boolean"
response = requests.get(url)
response.raise_for_status()
data = response.json()
question_list = data['results']
question_bank = []

#print(question_list)

for question in question_list:
    question_text = (question["question"])
    #print(question_text)
    question_answer = (question["correct_answer"])
    #print(question_answer)
    new_question = Question(question_text,question_answer)
    question_bank.append(new_question)


quiz = quiz_brain(question_bank)

while quiz.still_has_questions():

    quiz.next_question()

