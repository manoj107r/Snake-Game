import turtle
SNAKE_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIST = 20


class Snake:
    def __init__(self) -> None:
        self.snake_segments = []
        self.create_snake()
        self.head = self.snake_segments[0]

    def create_snake(self):
        for snake_position in SNAKE_POSITIONS:
            self.add_segment(snake_position)

    def move_snake(self):
        for snake_segment_pos in range(len(self.snake_segments)-1, 0, -1):
            new_x = self.snake_segments[snake_segment_pos-1].xcor()
            new_y = self.snake_segments[snake_segment_pos-1].ycor()
            self.snake_segments[snake_segment_pos].goto(new_x, new_y)
        self.head.forward(MOVE_DIST)

    def add_segment(self, snake_position):
        snake_segment = turtle.Turtle(shape="square")
        snake_segment.color("white")
        snake_segment.penup()
        snake_segment.goto(snake_position)
        self.snake_segments.append(snake_segment)

    def extend(self):
        self.add_segment(self.snake_segments[-1].position())

    def reset(self):
        for snake_seg in self.snake_segments:
            snake_seg.goto(1000, 1000)
        self.snake_segments.clear()
        self.create_snake()
        self.head = self.snake_segments[0]

    def move_up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def move_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def turn_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def turn_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
