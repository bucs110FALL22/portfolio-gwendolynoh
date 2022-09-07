import turtle 
myturtle = turtle.Turtle()

window = turtle.Screen()

myturtle.shape("turtle")
myturtle.color("purple")

myturtle.left(90)
for i in range(4):
  myturtle.forward(50)
  myturtle.left(90) 

myturtle.color("red")
myturtle.up()
myturtle.right(90)
myturtle.forward(50)
myturtle.down()

for i in range(4):
  myturtle.forward(50)
  myturtle.left(90)


window.exitonclick()

