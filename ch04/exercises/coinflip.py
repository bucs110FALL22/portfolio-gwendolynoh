import turtle
import random 
 
t = turtle.Turtle()
t.shape("turtle")
wn = turtle.Screen()


t.shape('turtle')
distance = 10
angle = (90)
in_screen = True

while in_screen:
  coin = random.randrange(0,2)
  if coin == 0:
    t.left(angle)
  else:
    t.right(angle)
  t.forward(distance)

  turtlex = t.xcor()
  turtley = t.ycor()

  x_range = wn.window_width()/2
  y_range = wn.window_height()/2

  if abs(turtlex) > x_range or abs(turtley) > y_range:
    in_screen = False

wn.bgcolor("light blue")
wn.exitonclick()







