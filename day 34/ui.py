from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 15, "italic")


class QuizInterface():
    def __init__(self, quiz_brain: QuizBrain):
        self.is_correct = None
        self.q_text = None
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(
            text=f"Score: 0",
            highlightthickness=0,
            bg=THEME_COLOR,
            fg="#ffffff")
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="#ffffff", bd=20, highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, text="Some questions", width=260, font=FONT)
        self.canvas.grid(column=0, row=1, columnspan=2, padx=50, pady=50)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, bg=THEME_COLOR, highlightthickness=0,
                                  command=lambda: self.check("True"))
        self.true_button.grid(column=0, row=2, pady=20, padx=20)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, bg=THEME_COLOR, highlightthickness=0,
                                   command=lambda: self.check("False"))
        self.false_button.grid(column=1, row=2)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="#ffffff")
        if self.quiz.still_has_questions():
            self.q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=self.q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"Your score {self.quiz.score}\nGame end")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def check(self, arg):
        is_correct = self.quiz.check_answer(arg)
        self.feedback(is_correct)

    def feedback(self, is_correct: bool):
        if is_correct:
            self.canvas.config(bg="green")
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.config(bg="red")
        self.window.after(500, self.get_next_question)

    # def check_true(self):
    #     self.is_correct = self.quiz.check_answer(True)
    #     if self.is_correct:
    #         self.canvas.config(bg="#00FF00")
    #         self.score_label.config(text=f"Score: {self.quiz.score}")
    #         self.window.after(3000, self.get_next_question)
    #     else:
    #         self.canvas.config(bg="#FF3333")
    #         self.window.after(3000, self.get_next_question)
    #
    # def check_false(self):
    #     self.is_correct = self.quiz.check_answer(False)
    #     if self.is_correct:
    #         self.canvas.config(bg="#00FF00")
    #         self.score_label.config(text=f"Score: {self.quiz.score}")
    #         self.window.after(3000, self.get_next_question)
    #     else:
    #         self.canvas.config(bg="#FF3333")
    #         self.window.after(3000, self.get_next_question)
