from turtle import Turtle
class Score(Turtle):
  def __init__(self):
    super().__init__()
    with open("highscore.txt", mode='r') as file:
      fileScore = file.read()
    self.penup()
    self.score = 0
    self.color("black")
    self.setposition(0.00, 250)
    self.hideturtle()
    self.high_score = int(fileScore)


    
  def updateScore(self):
    self.clear()
    self.write(f"Score: {self.score} High Score: {self.high_score}", font=('Arial', 20, 'normal'),align="center")

  def gameOver(self):
    if self.score > self.high_score:
      self.high_score = self.score 
      with open("highscore.txt", mode='w') as file:
        file.write(f"{self.score}")
    self.updateScore()
    self.score = 0
    
  
  def increase_score(self):
    self.score += 1
    self.updateScore()
    
