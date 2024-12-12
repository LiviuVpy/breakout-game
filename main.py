from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from bricks import BricksConstructor
from scoreboard import Scoreboard


MISS_LIMIT = -335
BRICK_DIST_LIMIT = 20

screen = Screen()
screen.setup(width=600, height=800)
screen.title("Breackout Game")
screen.bgcolor("black")
screen.tracer(0)

paddle = Paddle()
ball = Ball()
bricks_constructor = BricksConstructor()
bricks_constructor.create_bricks()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(paddle.move_right, "Right")
screen.onkeypress(paddle.move_left, "Left")

game_is_on = True
while game_is_on:
    
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with side walls:
    if ball.xcor() < -280 or ball.xcor() > 280:
        ball.bounce_x()

    # detect collision with the top wall:
    if ball.ycor() > 380:
        ball.bounce_y()

    # detect collision with the paddle:
    if ball.distance(paddle) < 23 and ball.ycor() < -315:
        ball.bounce_y()

    # detect paddle miss:
    if ball.ycor() < MISS_LIMIT:
        ball.reset_position()
        scoreboard.substract_lives()
            
    # detect collision with bricks:
    for brick in bricks_constructor.bricks:
        if ball.distance(brick) < BRICK_DIST_LIMIT:
            ball.bounce_y()
            bricks_constructor.delete_brick(brick)
            bricks_constructor.bricks.remove(brick)
            scoreboard.increase_score(brick)
            ball.increase_speed()

    # game_over:
    if scoreboard.lives < 1:
        game_is_on = False
        game_is_over = True       
            
    # game won:
    if len(bricks_constructor.bricks) == 0:
        game_is_on = False
        game_is_over = True


while game_is_over:

    time.sleep(ball.move_speed)
    screen.update()
    scoreboard.reset_score()
    
    if len(bricks_constructor.bricks) == 0:
        scoreboard.game_won()
    elif len(bricks_constructor.bricks) > 0:
        scoreboard.game_over()
    ball.move()
    paddle.paddle_enlarge() 

    # bounce bottom:
    if ball.ycor() < -315:
        ball.bounce_y()

    # bounce from top wall:
    if ball.ycor() > 380:
        ball.bounce_y()
        
    # bounce from side walls:
    if ball.xcor() < -280 or ball.xcor() > 280:
        ball.bounce_x()

    # bounce from bricks:
    for brick in bricks_constructor.bricks:
        if ball.distance(brick) < BRICK_DIST_LIMIT:
            ball.bounce_y()
      
            
screen.exitonclick()





