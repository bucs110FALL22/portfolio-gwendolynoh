import turtle 
myturtle = turtle.Turtle()

window = turtle.Screen()

myturtle.shape("turtle")
myturtle.color("red")

numsides = int(input("How many sides?"))
length = int(input("How long is each side?"))

for i in range(numsides):
  myturtle.forward(length)
  myturtle.left(360/numsides)
 
      

window.exitonclick()

