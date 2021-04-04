# from turtle import Turtle

# class Snake:
#     def __init__(self):
#         starting_positions = [(0, 0), (-20, 0), (-40, 0)]
#         self.segments = []

#         for position in starting_positions:
#             new_segment = Turtle("square")
#             new_segment.color("white")
#             new_segment.penup()
#             new_segment.goto(position)
#             self.segments.append(new_segment)

#     # for seg in segments:
#     #     seg.forward(20)
#     # for seg_num in range(start=2, stop=0, step=1)
#     # Range function couldn't take any keyword arguments.
#     # for seg_num in range(len(segments) - 1, 0, -1):
#     # So we can use the code on any number of segments.
#     def move(self):
#         for seg_num in range(len(self.segments) - 1, 0, -1):
#             new_x = self.segments[seg_num - 1].xcor()
#             new_y = self.segments[seg_num - 1].ycor()
#             self.segments[seg_num].goto(new_x, new_y)
#         self.segments[0].forward(20)

# Solution: 

from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)
