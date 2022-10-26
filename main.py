from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for q in question_data:
    new_q = Question(q["question"], q["correct_answer"])
    question_bank.append(new_q)


this_quiz = QuizBrain(question_bank)
this_quiz.start_quiz()

