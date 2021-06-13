from turtle import Screen, Turtle

# according to the turtle coordinate frame
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self, user_color):
        self.segments = []
        self.cur_speed = "normal"
        self.head = None
        self.user_color = user_color
        self.create_snake()

    def create_snake(self):
        x = 0
        for i in range(0, 3):
            new_segment = Turtle(shape="square")
            new_segment.color(self.user_color)
            new_segment.penup()
            new_segment.goto(x, 0)
            new_segment.speed(self.cur_speed)
            self.segments.append(new_segment)
            x -= 20
        self.head = self.segments[0]

    def move(self):
        # reverse traversal, will replace each one by one
        for seg_num in range(len(self.segments) - 1, 0, -1):
            self.segments[seg_num].speed(self.cur_speed)
            self.segments[seg_num].goto(self.segments[seg_num - 1].xcor(),
                                        self.segments[seg_num - 1].ycor())

        self.segments[0].forward(20)

    # if conditions used to prohibit backwards movement
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

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color(self.user_color)
        new_segment.penup()
        new_segment.goto(position)
        new_segment.speed(self.cur_speed)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def inc_speed(self, new_speed):
        self.cur_speed = new_speed


    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()

