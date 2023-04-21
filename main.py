from turtle import Screen
from snake_appearance import Snake,Borders
from food import Food
from scoreboard import Score
import time

game_over = False

screen = Screen()
screen.screensize(canvwidth=700, canvheight=700)
screen.bgcolor("black")
screen.title("Feed Sonic the snake")
# .tracer(0) means
screen.tracer(0)

sonic = Snake()
food = Food()
scoreboard = Score()
border = Borders()
# The snake need to respond to user input on keyboard
# Use screen.listen() and screen.onkey()

screen.listen()
screen.onkey(sonic.turn_up, "Up")
screen.onkey(sonic.turn_down, "Down")
screen.onkey(sonic.turn_left, "Left")
screen.onkey(sonic.turn_right, "Right")

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
    if sonic.head.xcor() > 340 or sonic.head.xcor() < -340\
            or sonic.head.ycor() > 340 or sonic.head.ycor() < -340:
        scoreboard.reset_score()
        game_over = True

        # Detect if the head hit any part of the body = Game Over
        for segment in sonic.segments:
            if segment == sonic.head:
                pass
            if sonic.head.distance(segment) < 15:
                scoreboard.reset_score()
                game_over = True

        for segment in sonic.segments[1:]:
            if sonic.head.distance(segment) < 15:
                scoreboard.reset_score()
                game_over = True

screen.exitonclick()
