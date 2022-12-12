import pygame 
import random 
import math

#Part A
pygame.display.init()
screen_width = 400
screen_height = 400
window = pygame.display.set_mode([screen_width,screen_height])
window_size = pygame.display.get_window_size()

color = "light green"
window.fill(color)
pygame.display.flip()

x = 200
y = 200
center = (x,y)
pygame.draw.circle(window,"pink",center,200)
pygame.display.flip()

x1 = 0
y1 = 200
x2 = 400
y2 = 200
start_pos1 = (x1,y1)
end_pos1 = (x2,y2)
pygame.draw.line(window,"black",start_pos1, end_pos1, width=2)
pygame.display.flip()

x3 = 200
y3 = 400
x4 = 200
y4 = 0
start_pos2 = (x3,y3)
end_pos2 = (x4,y4)
pygame.draw.line(window,"black",start_pos2, end_pos2, width=2)
pygame.display.flip()

#Part B
for i in range(10):
  x5 = random.randrange(0,400)
  y5 = random.randrange(0,400)
  coord = (x5,y5)
  distance_from_center = math.hypot(x5-x, y5-y)
  is_in_circle = distance_from_center <= screen_width/2
  if is_in_circle == True:
    pygame.draw.circle(window,"purple",coord,10)
    pygame.display.flip()
    pygame.time.wait(500)
  if is_in_circle == False:
    pygame.draw.circle(window,"red",coord,10)
    pygame.display.flip()
    pygame.time.wait(500)
pygame.display.flip()
pygame.time.wait(1000)

#Part C
window.fill("black")
playerChoice = ""
leftrect = pygame.Rect(0 , 0, x/2, y)
rightrect = pygame.Rect(x/2, 0 , x/2 , y)
redteam = pygame.draw.rect(window ,"red",leftrect)
blueteam = pygame.draw.rect(window ,"blue",rightrect)
pygame.display.flip()

print("Guess who will win?")
print("red or blue team?")
pygame.time.wait(7000)

window.fill("black")
pygame.display.flip()
pygame.time.wait(2000)

#Player_red vs player_blue
pygame.display.init()
screen_width = 400
screen_height = 400
window = pygame.display.set_mode([screen_width,screen_height])
window_size = pygame.display.get_window_size()

color = "light green"
window.fill(color)
pygame.display.flip()

x = 200
y = 200
center = (x,y)
pygame.draw.circle(window,"pink",center,200)
pygame.display.flip()

x1 = 0
y1 = 200
x2 = 400
y2 = 200
start_pos1 = (x1,y1)
end_pos1 = (x2,y2)
pygame.draw.line(window,"black",start_pos1, end_pos1, width=2)
pygame.display.flip()

players = ["red","blue"]
red_score = 0
blue_score = 0

for n in range(10):
  for player in players:
    x5 = random.randrange(0,400)
    y5 = random.randrange(0,400)
    coord = (x5,y5)
    distance_from_center = math.hypot(x5-x, y5-y)
    is_in_circle = distance_from_center <= screen_width/2
    if is_in_circle == True:
      print(player,"hit")
      pygame.draw.circle(window,player,coord,10)
      pygame.draw.circle(window,player,coord,10)
      if player is players[0]:
          red_score += 1
      if player is players[1]:
          blue_score += 1
      pygame.display.flip()
      pygame.time.wait(500)
    if is_in_circle == False:
      print(player,"miss")
      pygame.draw.circle(window,"grey",coord,10)
      pygame.display.flip()
      pygame.time.wait(500)
  if n == 9:
      if red_score > blue_score:
        print(player[0],"Is the winner")
      if red_score < blue_score:
        print(player[1],"Is the winner")
      if red_score == blue_score:
        print("Tie")
      pygame.time.wait(1000)
    
pygame.display.flip()
pygame.time.wait(2000)


Guess = True
while Guess == True:
  for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONDOWN:
      if event.pos[0] < x / 2:
        playerchoice = "red"
        Guess = False
      elif event.pos[0] > x / 2:
        playerchoice = "blue"
        Guess = False 
print("you choose",playerchoice)
pygame.display.flip()
pygame.time.wait(1000)


if Guess is playerchoice:
  print("you're right")
else: 
  print("you're wrong")
pygame.time.wait(1000)

