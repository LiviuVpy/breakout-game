from turtle import Turtle

LIVES = 5
FONT = ('Courier', 12, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        
        self.color('white')
        self.penup()
        self.hideturtle()
        self.score = 0
        self.lives = LIVES
        self.high_score = self.get_hight_score()
        self.update_scoreboard()
        

    def update_scoreboard(self):
        self.clear()
        self.goto(-250, 350)
        self.write(f'SCORE: {self.score} HIGH SCORE {self.high_score}', align = "left", font=FONT)
        self.goto(250, 350)
        self.write(f'LIVES: {self.lives}', align = "right", font=FONT)

    def increase_score(self, brick_obj):
        if brick_obj.color()[0] == "firebrick1":
            self.score += 7
        if brick_obj.color()[0] == 'DarkOrange1':
            self.score += 5
        if brick_obj.color()[0] == 'LightGreen':
            self.score += 3
        if brick_obj.color()[0] == 'LightGoldenrod1':
            self.score += 1
        self.update_scoreboard()

    def substract_lives(self):
        self.lives -= 1
        self.update_scoreboard()

    def reset_score(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
        self.score = 0
        self.write_high_score()
        

    def get_hight_score(self):
        with open('D:\\ITwork\\PORTOFOLIO\\breakout_game\\high_score.txt', 'r') as file:
            contents = file.read()
            return contents
        
    def write_high_score(self):
        with open('D:\\ITwork\\PORTOFOLIO\\breakout_game\\high_score.txt', 'w') as file:
            file.write(str(self.high_score))
            

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', align = "center", font=('Courier', 24, 'normal'))
   

    def game_won(self):
        self.goto(0, 0)
        self.write('YOU WON!', align = "center", font=('Courier', 24, 'normal'))
      


        

    

       
