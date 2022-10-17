from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for q in question_data:
    # print(i)
    # print(question_data[i])
    # print(q["text"])
    new_q = Question(q["text"], q["answer"])
    question_bank.append(new_q)

# print(question_bank)
# print(question_bank[0].text)

this_quiz = QuizBrain(question_bank)
this_quiz.start_quiz()

