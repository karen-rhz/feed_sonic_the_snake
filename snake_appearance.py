from turtle import Turtle, Screen

INITIAL_POSITIONS = [(-40, 0), (-20, 0), (0, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
screen = Screen()
screen.colormode()


class Snake(Turtle):

    def __init__(self):
        super().__init__()
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in INITIAL_POSITIONS:
            self.grow_snake(position)

    def grow_snake(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("lime green")
        new_segment.penup()
        # Each square is 20px by 20px
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend_snake(self):
        self.grow_snake(self.segments[-1].position())

    def move(self):
        # for segments in range(start=2 ,stop=0 ,step=-1)
        # We want 2, 1, 0
        # start = first value of range
        # stop = last value of range
        # step = how do we get from start to stop
        for segment_number in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment_number - 1].xcor()
            new_y = self.segments[segment_number - 1].ycor()
            self.segments[segment_number].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def turn_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def turn_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def turn_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def turn_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)