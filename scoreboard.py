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
        with open("high_score.txt") as high_score_file:
            self.high_score = int(high_score_file.read())
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
        self.keep_high_score()
        self.score = 0
        self.refresh_scoreboard()

    def keep_high_score(self):
        # Keeping tabs on the new high score
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", mode="w") as high_score_file:
                high_score_file.write(f"{self.high_score}")
        else:
            pass