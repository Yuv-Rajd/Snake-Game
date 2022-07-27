from turtle import Turtle
ALLIGNMENT="center"
FONT=("Courier",22,"normal")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score :{self.score}",align=ALLIGNMENT,font=FONT)

    def inccrease_score(self):
        self.score +=1
        self.clear()
        self.update_scoreboard()
        
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align=ALLIGNMENT,font=FONT)
