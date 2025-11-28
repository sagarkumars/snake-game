from turtle import Turtle

ALIGN = "center"
FONT = "Ärial"


def read_score_from_file():
    with open("data.txt") as file:
        content = file.read()
        return int(content)


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = read_score_from_file()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def write_score_to_file(self):
        with open("data.txt", mode="w") as file:
            file.write(f"{self.high_score}")

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score {self.score} : High Score {self.high_score}", align=ALIGN, font=(FONT, 24, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_score_to_file()
        self.score = 0
        self.update_scoreboard()
