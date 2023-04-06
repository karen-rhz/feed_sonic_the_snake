from turtle import Turtle, Screen

INITIAL_POSITIONS = [(-40, 0), (-20, 0), (0, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
screen = Screen()
screen.colormode()


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def appearance_head(self):
        sonic_whole_head = []
        # Tongue of snake
        sonic_tongue = Turtle("square")
        sonic_tongue.penup()
        sonic_tongue.color("red")
        sonic_tongue.shapesize(0.2, 0.5)
        sonic_tongue.goto(10, 0)
        sonic_whole_head.append(sonic_tongue)

        # Head of snake
        sonic_head = Turtle("triangle")
        sonic_head.color("lime green")
        sonic_whole_head.append(sonic_head)

        # Eye of snake
        sonic_eye_positions = [(1, 8), (1, -8)]
        for n in range(2):
            sonic_eye = Turtle("circle")
            sonic_eye.penup()
            sonic_eye.color("yellow")
            sonic_eye.shapesize(0.4, 0.4)
            sonic_eye.goto(sonic_eye_positions[n])
            sonic_whole_head.append(sonic_eye)
        # So the whole list can be treated as 1 turtle object instead of 3 separate ones
        sonic_whole_head = Turtle()
        sonic_whole_head.goto(INITIAL_POSITIONS[2])
        self.segments.append(sonic_whole_head)

    def create_snake(self):
        for position in INITIAL_POSITIONS[:2]:
            self.grow_snake(position)
        # Can't run the rest of the code bc the head is not properly set up
        # The head stays at (0, 0) while the whole body is moving as expected
        self.appearance_head()

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

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
