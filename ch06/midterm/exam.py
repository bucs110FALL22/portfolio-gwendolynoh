import turtle

# Screen
screen = turtle.Screen()
screen.bgcolor("light green")
pen = turtle.Turtle()


# Bow
def bow(bow_color, string):
  '''
  This function uses turtle to draw a half ciricle as the outline of the bow it then completes it by adjusting the width and changing the color of the draw line to act as the "string" to the bow 
  '''
  pen.up()
  pen.goto(-100, 0)
  pen.down()
  pen.color(bow_color)
  pen.width(5)
  pen.circle(100, 180)
  pen.width(1)
  pen.color(string)
  pen.goto(-100, 0)


# Arrow
def arrow(arrow_line):
  '''
The arrow function uses turtle to draw a red line and then uses different angles to position the turtle in the right place to form a equilateral triangle to act like an "arrow head"
  '''
  length = 10
  pen.up()
  pen.goto(-150, 100)
  pen.down()
  pen.color(arrow_line)
  pen.width(3)
  pen.backward(180)
  pen.right(270)
  pen.goto(30, 105)
  for i in range(3):
    pen.forward(length)
    pen.left(120)

# Target
def target(target_outer_color, circle_1, circle_2, circle_3):
  '''
This function is more than 10 lines because it repeats the circle code 3 time inorder to form smaller circles. The main purpose of this function is to create the "target" for the bow and arrow. First the turtle is used to draw a white square and with in it is different sized circles with different colors to represent the point system in a tradition archery game. 
  '''
  length = 200
  pen.color(target_outer_color)
  pen.up()
  pen.goto(150, 200)
  pen.down()
  pen.color(target_outer_color)
  pen.begin_fill()
  for i in range(4):
    pen.forward(length)
    pen.left(90)
  pen.end_fill()
  pen.up()
  #Circle 1
  pen.fillcolor(circle_1)
  pen.begin_fill()
  pen.goto(150, 100)
  pen.down()
  pen.circle(100, 360)
  pen.end_fill()
  pen.up()
  # Circle 2
  pen.fillcolor(circle_2)
  pen.begin_fill()
  pen.goto(200, 100)
  pen.down()
  pen.circle(50, 360)
  pen.end_fill()
  pen.up()
  # Circle 3
  pen.fillcolor(circle_3)
  pen.begin_fill()
  pen.goto(230, 100)
  pen.down()
  pen.circle(20, 360)
  pen.end_fill()
  # Position
  end_position = print("The End Position is:",pen.pos())
  return end_position
  
def main():
  '''
This is the "main" function that calls all the other functions. In my main I also included my parameters for the other functions
  '''
  bow_color = "black"
  string = "white"
  bow(bow_color, string)

  arrow_line = "red"
  arrow(arrow_line)

  target_outer_color = "white"
  circle_1 = "blue"
  circle_2 = "red"
  circle_3 = "black"
  target(target_outer_color, circle_1, circle_2, circle_3)

main()

screen.exitonclick()
