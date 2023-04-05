from turtle import Turtle
ALIGNEMENT = "center"
FONT = ("Arial", 15, "bold")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 320)
        self.score = 0
        self.refresh_scoreboard()

    def refresh_scoreboard(self):
        self.write(arg=f"Score: {self.score}",
                   align=ALIGNEMENT,
                   font=FONT)

    def new_score(self):
        self.score += 1
        self.clear()
        self.refresh_scoreboard()

    def game_over(self):
        self.home()
        self.write("Game Over.", align=ALIGNEMENT, font=FONT)