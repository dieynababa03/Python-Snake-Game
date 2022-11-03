from turtle import Screen, Turtle
from snake import Snake
from dot import Dot
from score import Score
import time
#screen setup
screen = Screen()
screen.bgcolor("white")
screen.title("Welcome to my snake game!")
screen.setup(width=600, height=600)
screen.tracer(0)

#creating snake from Snake object
snake = Snake()
screen.listen()
screen.onkey(key="Up", fun=snake.moveUp)
screen.onkey(key="Down", fun=snake.moveDown)
screen.onkey(key="Left", fun=snake.moveLeft)
screen.onkey(key="Right", fun=snake.moveRight)

#collision object
object = Dot()
scoreBoard = Score()
gameOver = Score()

coordinates = 0
gameRunning = True
snake.create_snake()
screen.update()
while gameRunning:
  screen.update()
  time.sleep(0.1)
  snake.moveSnake()

  if snake.my_snake[0].distance(object) < 20:
    object.newPos()
    scoreBoard.increase_score()
    snake.addToSnake()
  
  if snake.my_snake[0].xcor() > 290 or snake.my_snake[0].xcor() < -290 or snake.my_snake[0].ycor() > 290 or snake.my_snake[0].ycor() < -290:
    scoreBoard.gameOver()
    snake.reset()
    
  
  for head in snake.my_snake[1:]:
    if snake.my_snake[0].distance(head) < 10:
      scoreBoard.gameOver()
      snake.reset()
      



    


# to check for collision check if turtles x/y value
# exceeds end of screen
















screen.exitonclick()

