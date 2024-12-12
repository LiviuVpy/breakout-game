from turtle import Turtle

STARTING_MOVE_DISTANCE = 10
SPEED_ACC = 0.9


class Ball(Turtle):
    def __init__(self):
        super().__init__()

        self.shape('circle')
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color('white')
        self.penup()
        self.x_move = STARTING_MOVE_DISTANCE
        self.y_move = STARTING_MOVE_DISTANCE
        self.move_speed = 0.1


    def move(self):
        new_x = self.xcor() - self.x_move
        new_y = self.ycor() - self.y_move
        self.goto(new_x, new_y)

    def bounce_x(self):
        self.x_move *= -1

    def bounce_y(self):
        self.y_move *= -1

    def reset_position(self):
        self.goto(0,0)
        self.move_speed = 0.1
        if self.ycor() > 0:
            self.bounce_y()
    
    def increase_speed(self):
        self.move_speed *= SPEED_ACC
        