from turtle import Turtle

WIDTH = 600
HEIGHT = 800
BRICKS_COLORS = ['firebrick1', 'firebrick1', 'DarkOrange1', 'DarkOrange1', 'LightGreen', 'LightGreen', 'LightGoldenrod1', 'LightGoldenrod1']
X = -275
Y = 270


class BricksConstructor():
    def __init__(self):
        self.bricks = []


    def create_bricks(self):
        for i in range(len(BRICKS_COLORS)):
            for j in range(WIDTH//45):
                new_y = Y - i * 15 
                new_x = X + j * 45 
                new_brick = Turtle('square')
                new_brick.penup()
                new_brick.goto(new_x, new_y)
                new_brick.color(BRICKS_COLORS[i])
                new_brick.shapesize(stretch_wid=0.5, stretch_len=2)
                self.bricks.append(new_brick)
  
    def delete_brick(self, brick):
        brick.penup()
        brick.goto(660,860)




    




