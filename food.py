from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("yellow")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed("fastest")
        self.new_food_position()

    def new_food_position(self):
        cor_x = random.randint(-280, 280)
        cor_y = random.randint(-280, 280)
        self.goto(cor_x, cor_y)