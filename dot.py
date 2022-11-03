from turtle import Turtle
import random
class Dot(Turtle):
  def __init__(self):
    super().__init__()
    self.shape("turtle")
    self.penup()
    self.shapesize(0.8, 0.8)
    self.color("green")
    self.speed(0)
    self.setposition(random.randint(-250, 250), random.randint(-250, 250))
  def newPos(self):
    self.setposition(random.randint(-250, 250), random.randint(-250, 250))