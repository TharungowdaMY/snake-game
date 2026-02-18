from turtle import Screen
from snake import Snake
from FOOD import Food
from scoreboard import Scoreboard

import time
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("SNAKE GAME")
screen.tracer(0)#it will skip the animation
snake=Snake()
food=Food()
scoreboard=Scoreboard()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")



game_is_on=True
while game_is_on:
    screen.update()#it will update the screen AFTER EACH STEP
    time.sleep(0.1)  # it will delay 0.1 sec for each step

    snake.move()
 #detect collision with food
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    #DETECTION COLLIDION WITH WALL
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        scoreboard.reset()
        snake.reset()    #DETECT OF HEAD COLLOsIon WITH A TAIL
    for segment in snake.segments[-1:]:

        if segment==snake.head:
            pass
        elif snake.head.distance(segment)<10:
            scoreboard.reset()

screen.exitonclick()