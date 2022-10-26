
class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_ans(self, user_answer, correct_answer):
        return user_answer.lower() == correct_answer.lower()

    def start_quiz(self):
        print(f"Starting Quiz. There are {len(self.question_list)} questions. Type 'quit' to exit.")
        while self.still_has_questions():
            current_q_num = self.question_number
            self.question_number += 1
            current_q = self.question_list[current_q_num].text
            current_ans = self.question_list[current_q_num].answer

            user_answer = input(f"Q.{self.question_number}: {current_q}(True/False): ")
            if user_answer == "quit":
                break
            if self.check_ans(user_answer, current_ans):
                print("correct")
                self.score += 1
            else:
                print(f"incorrect. The answer is: {current_ans}")

            print("")
        print(f"___________________________________")
        print(f"Your final score is {self.score} out of {self.question_number}. Goodbye!")


