# > Day 20 -------------------------------------------------------------------------------------------------------------
# > 1. Snake.py - Snake Game Project -----------------------------------------------------------------------------------

from turtle import Turtle

# Snake Constant Variables
# Initial Snake Length.
SNAKE_LENGTH = 3
# Initial Snake Segment Position on X for the first one.
SEGMENT_POS_X = 0
# Additional Snake Position on X for the others.
SET_SEG_POS_X = 20
# Move Snake by Int Pixels. ATTENTION: SET_SEG_POS_X it's need to be equal to MOVE_DISTANCE for not act awkward.
MOVE_DISTANCE = 20

# Snake Directions
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    # Snake Settings
    def __init__(self):
        self.snake_body = []
        self.segment_pos_x = SEGMENT_POS_X
        self.set_seg_pos_x = SET_SEG_POS_X
        self.create_snake()
        self.head = self.snake_body[0]

    # Create Snake Segments Objects and Set Start Position for each
    def create_snake(self):
        for segment in range(SNAKE_LENGTH):
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(x=self.segment_pos_x, y=0)

            self.snake_body.append(new_segment)
            self.segment_pos_x -= self.set_seg_pos_x

    # Move Snake Function
    def move(self):
        for seg_num in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[seg_num - 1].xcor()
            new_y = self.snake_body[seg_num - 1].ycor()
            self.snake_body[seg_num].goto(new_x, new_y)

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
# ----------------------------------------------------------------------------------------------------------------------