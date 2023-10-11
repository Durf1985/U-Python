import random


class Quiz:
    def __init__(self, question_bank):
        self.question_bank = question_bank
        self.question_number = 1
        self.used_list = []

    def not_in_list(self, question):
        if question not in self.used_list:
            self.used_list.append(question)
            self.question_number += 1
            return True
        else:
            return False

    def get_question(self):
        return random.choice(self.question_bank)

    def is_correct(self, right_answer, answer):
        if right_answer.lower() == answer.lower():
            return True
        else:
            self.question_number = 1
            self.used_list = []
            print(f"Your right answer chain is broken")
            return False

    def end_game(self, decision):
        if decision == "end":
            return False
