from turtle import Turtle

MOVE_DISTANCE = 40
START_POSITION = (0, -330)

class Paddle(Turtle):
    def __init__(self):
        super().__init__()

        self.shape('square')
        self.color('skyblue')
        self.shapesize(stretch_wid=0.5, stretch_len=2)
        self.penup()
        self.goto(START_POSITION)
        

    def move_right(self):
        if self.xcor()  < 270:
            new_x = self.xcor() + MOVE_DISTANCE
            self.goto(new_x, self.ycor())

    def move_left(self):
        if self.xcor() > -280:
            new_x = self.xcor() - MOVE_DISTANCE
            self.goto(new_x, self.ycor())
    
    def paddle_enlarge(self):
        self.shapesize(stretch_wid=0.5, stretch_len=300)
        self.goto(START_POSITION)