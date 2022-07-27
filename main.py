from turtle import Screen, position
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


screen =Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake= Snake()
food=Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #detect collision
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.inccrease_score()


    #detect collision with walll
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        game_is_on=False
        scoreboard.game_over()




screen.exitonclick()