import turtle 

window = turtle.Screen()

def drawEqShape(myturtle = None, num_sides=0,side_length=0):
  myturtle = turtle.Turtle()
  myturtle.shape("turtle")
  myturtle.color("green")
  num_sides = int(input("How many sides?"))
  side_length = int(input("How long are each sides?"))
  
  for i in range(num_sides):
    myturtle.forward(side_length)
    myturtle.left(360/num_sides)
drawEqShape(1,2,3)


window.exitonclick()