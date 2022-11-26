import turtle
import random
import time

#setup window
wn = turtle.Screen()
wn.bgcolor('green')
wn.setup(width=800, height=600)
wn.title('Tank Assault')
wn.register_shape('tank.gif')
wn.register_shape('enemyship.gif')
wn.tracer(0)

#setup player tank
player = turtle.Turtle()
player.penup()
player.shape('tank.gif')
player.color('green')
player.speed(1)

#create enemy tanks
enemies = []
difficulty = 5
for i in range(difficulty):
  newEnemy = turtle.Turtle()
  newEnemy.shape('enemyship.gif')
  newEnemy.speed('fastest')
  newEnemy.penup()
  newEnemy.setpos(random.randint(-400, 400), random.randint(-300, 300))
  enemies.append(newEnemy)

#set up cannon
cannon = turtle.Turtle()
cannon.shape('triangle')
cannon.shapesize(1, 10)
cannon.color('purple')
cannon.penup()
cannon.seth(90)
cannon.speed('fastest')

#player and cannon movement functions
def cannonRight():
  cannon.right(10)

def cannonLeft():
  cannon.left(10)

def forward():
  player.seth(90)
  player.forward(20)

def backward():
  player.seth(270)
  player.forward(20)

#add missiles here
missiles = []

def fireMissile():
  #create missiles
  newMissile = turtle.Turtle()
  newMissile.shape('square')
  newMissile.shapesize(0.3, 2)
  newMissile.speed('fastest')
  newMissile.penup()
  missiles.append(newMissile)
  newMissile.hideturtle()
  newMissile.setpos(cannon.xcor(), cannon.ycor())
  newMissile.seth(cannon.heading())
  newMissile.showturtle()
  
#create a useful function to see if 2 objects are colliding(will need for later)
def isCollision(object1, object2):
  if object1.distance(object2) < 50:
    return True

#set up score
score = 0
highScore = 0
scorePen = turtle.Turtle()
scorePen.speed('fastest')
scorePen.color('red')
scorePen.hideturtle()
scorePen.penup()
scorePen.goto(-350, 230)
scorePen.write(f'SCORE: {score},    HIGH SCORE: {highScore}', font=('Arial', 30))

#main loop
while True:
  for missile in missiles:
    missile.forward(15)

  #make cannon follow player tank
  x = player.xcor()
  y = player.ycor()
  cannon.setpos(x, y-10)

  #make enemy move towards player
  for enemy in enemies:
    enemy.seth(enemy.towards(player))
    enemy.forward(0.2)

  #check if missile hit enemy
  for enemy in enemies:
    for missile in missiles:
      if isCollision(enemy, missile):
        enemy.hideturtle()
        enemy.setpos(random.randint(-400, 400), random.randint(-300, 300))
        enemy.showturtle()
        score += 100
        if score > highScore:
          highScore = score

        scorePen.undo()
        scorePen.goto(-350, 230)
        scorePen.write(f'SCORE: {score}, HIGH SCORE: {highScore}', font=('Arial', 30))

  #check if enemy hit player
  for enemy in enemies:
    if isCollision(enemy, player):
      player.hideturtle()
      cannon.hideturtle()
      player.setpos(0, 0)
      player.showturtle()
      cannon.showturtle()
      enemy.hideturtle()
      enemy.setpos(random.randint(-400, 400), random.randint(-300, 300))
      enemy.showturtle()
      score = 0
      scorePen.undo()
      scorePen.goto(-350, 230)
      scorePen.write(f'SCORE: {score}, HIGH SCORE: {highScore}', font=('Arial', 30))
      time.sleep(3)

  #check if player is on boundaries to scroll
  if player.ycor() > 300:
    player.sety(-300)
    
  elif player.ycor() < -300:
    player.sety(300)
      
  #player keybinds
  wn.listen()
  wn.onkeypress(forward, 'Up')
  wn.onkeypress(backward, 'Down')
  wn.onkeypress(forward, 'r')
  wn.onkeypress(backward, 'f')
  wn.onkeypress(cannonLeft, 'a')
  wn.onkeypress(cannonRight, 'd')
  wn.onkeypress(fireMissile, 'space')

  wn.update()
