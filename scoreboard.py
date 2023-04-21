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
        # Keeping track of highest score
        self.high_score = 0
        self.refresh_scoreboard()

    def refresh_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score}  Highest score: {self.high_score}",
                   align=ALIGNEMENT,
                   font=FONT)

    def new_score(self):
        self.score += 1
        self.refresh_scoreboard()

    # def game_over(self):
    #     self.home()
    #     self.reset_score()
    #     self.write("Game Over.", align=ALIGNEMENT, font=FONT)

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.refresh_scoreboard()