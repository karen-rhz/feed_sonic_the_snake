from turtle import Screen
from snake_appearance import Snake
from food import Food
from scoreboard import Score
import time

game_over = False

screen = Screen()
screen.screensize(canvwidth=600, canvheight=600)
screen.bgcolor("black")
screen.title("Feed Sonic the snake")
# .tracer(0) means
screen.tracer(0)

sonic = Snake()
food = Food()
scoreboard = Score()

# The snake need to respond to user input on keyboard
# Use screen.listen() and screen.onkey()

screen.listen()
screen.onkey(sonic.up, "Up")
screen.onkey(sonic.down, "Down")
screen.onkey(sonic.left, "Left")
screen.onkey(sonic.right, "Right")

# Snake needs to go forward by himself
while not game_over:
    screen.update()
    time.sleep(0.1)
    sonic.move()

    # Detect collision with food
    if sonic.head.distance(food) < 15:
        sonic.extend_snake()
        food.new_food_position()
        scoreboard.new_score()

    # Detect collision with wall = Game Over
    if sonic.head.xcor() > 320 or sonic.head.xcor() < -320\
            or sonic.head.ycor() > 320 or sonic.head.ycor() < -320:
        game_over = True
        scoreboard.game_over()

    # Detect if the head hit any part of the body = Game Over
    #     for segment in sonic.segments:
    #         if segment == sonic.head:
    #             pass
    #         if sonic.head.distance(segment) < 15:
    #             game_over = True
    #             scoreboard.game_over()

        for segment in sonic.segments[1:]:
            if sonic.head.distance(segment) < 15:
                game_over = True
                scoreboard.game_over()

screen.exitonclick()
