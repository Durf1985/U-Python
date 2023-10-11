from turtle import Turtle


ALIGN = "Left"
FONT = ('Arial', 10, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("C:\\Users\\Fallgeratoor\\Desktop\\score.txt") as score_file:
            save_high_score = score_file.read()
        self.high_score = int(save_high_score)
        self.penup()
        self.color("white")
        self.hideturtle()
        self.setpos(-290, 285)
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, ALIGN, FONT)

    def increase(self):
        self.score += 1
        self.clear()
        self.update()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("C:\\Users\\Fallgeratoor\\Desktop\\score.txt",mode="w") as file:
                file.write(str(self.high_score))

        self.score = 0
        self.update()

    # def game_over(self):
    #     self.setpos(-70, 0)
    #     self.clear()
    #     self.write(f"You lose, your score: {self.score}", False, ALIGN, FONT)
