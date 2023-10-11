from question_model import Question
from data import question_data
from quiz_brain import Quiz

question_bank = []
for i in question_data:
    new_Question = Question(i['category'], i['type'], i['question'], i['correct_answer'], i['incorrect_answers'])
    question_bank.append(new_Question)

is_continue_game = True
quiz_brain = Quiz(question_bank)

while is_continue_game:
    decision = input("If you don't want to play, then type 'no', or 'yes' if you want to play: ")
    if decision == "no":
        is_continue_game = False
    else:
        if quiz_brain.question_number > len(question_bank):
            break
        print(f"This is question number {quiz_brain.question_number}")
        question = quiz_brain.get_question()
        while not quiz_brain.not_in_list(question):
            question = quiz_brain.get_question()

        print(f"Right answer {question.correct_answer}")
        your_answer = input(f"{question.question} True or False? ")
        if quiz_brain.is_correct(question.correct_answer, your_answer):
            print("You are right.")
            print()
        else:
            print(f"You are wrong.")
            print()
