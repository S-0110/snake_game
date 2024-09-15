from turtle import Turtle
X_POSITION = [(0,0), (-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.all_turtle = []
        self.create_snake()
        self.head = self.all_turtle[0]

    def create_snake(self):
        for position in X_POSITION:
            self.add_segment(position)


    def add_segment(self, position):
        tim = Turtle(shape="square")
        tim.penup()
        tim.color("white")
        tim.goto(position)
        self.all_turtle.append(tim)




    # add snake length
    def extend(self):
        self.add_segment(self.all_turtle[-1].position())



    def move(self):
        # start = len(segment)-1, stop = 0, step =-1
        for number in range(len(self.all_turtle) - 1, 0, -1):
            new_x = self.all_turtle[number - 1].xcor()
            new_y = self.all_turtle[number - 1].ycor()
            self.all_turtle[number].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
