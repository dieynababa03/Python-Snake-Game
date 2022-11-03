from turtle import Screen, Turtle
class Snake:
  def __init__(self):
    self.my_snake = []
    self.coordinates = 0
    self.create_snake()
  
  #Creating my snake
  def create_snake(self):
    for i in range(0, 2):
      snake = Turtle(shape="square")
      snake.penup()
      snake.color("blue")
      snake.setpos(self.coordinates, 0.00)
      self.coordinates -= 20
      self.my_snake.append(snake)
  #Makes snake constantly move forward 20 steps

  def moveSnake(self):
    for i in range(len(self.my_snake) - 1, 0, -1):
      #setting coordinates for current snake im modifying
      #to move to the next part of the snake
      new_x = self.my_snake[i - 1].xcor()
      new_y = self.my_snake[i - 1].ycor()
      #telling snake to go to those coordinates
      self.my_snake[i].goto(new_x, new_y)
    self.my_snake[0].forward(20)
  
  #Setting up key functions
  def moveUp(self):
    if self.my_snake[0].heading() != 270:
      self.my_snake[0].setheading(90)
  def moveDown(self):
    if self.my_snake[0].heading() != 90:
      self.my_snake[0].setheading(270)
  def moveLeft(self):
    if self.my_snake[0].heading() != 0:
      self.my_snake[0].setheading(180)
  def moveRight(self):
    if self.my_snake[0].heading() != 180:
      self.my_snake[0].setheading(0)

  def addToSnake(self):
      snake = Turtle(shape="square")
      snake.penup()
      snake.color("blue")
      snake.setpos(self.coordinates, 0.00)
      self.coordinates -= 20
      self.my_snake.append(snake)

  def reset(self):
    for elements in self.my_snake:
      elements.goto(500, 500)
    self.my_snake.clear()
    self.create_snake()

  

    
