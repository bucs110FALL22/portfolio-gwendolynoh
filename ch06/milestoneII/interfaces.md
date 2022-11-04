# Final Project Milestone #2

[Final Project Description](https://docs.google.com/document/d/1j3zgypVjPjzXl4pL1_Wpjvp3GLCW9zcFydkwUjNfNUA/edit?usp=sharing)

Complete this document in **your** portfolio (CH 6). 

Let's decide on our Final project. Select the idea from Milestone 1 that seems the most interesting to you.

Each class is a model of some real world object. We often refer to data classes as the ***models*** in a GUI program. Your models represent your application data.

Given what you have learned about classes on Chapter 6, describe the ***interface only*** of 3 classes you think you might need for your project.

*For example*, if you want to create a space invaders type game, you would need a class to represent the ship, which could have an interface such as: 

* class ship
    * moveLeft()
    * moveRight()
    * shoot()

***

Come up with interfaces fot 3 possible classes you think you may need. Again, brainstorm a little. Nothing is *wrong*.

## Class Interface 1
class Riddle:
'''
The Riddle is placed at the end of each level to move on to more challanging levels in the game. It will uses text that displays the riddle using a random generator from a dictionary
'''
  def __init__(self):
    self.text = str()
    self.answer_space()
    self.random

## Class Interface 3
class Maze_lines:
'''
The Maze line creates the boarders in the game and is used as the "wall" on the surface so that creates the puzzle the players will have to solve. It uses Turtle to draw the lines on the game using position and the turtle interface. 
'''
  def __init__(self):
    self.pen = turtle.Turtle()
    self.pen_goto = (x,y)
    self.forward()
    self.backward()
    self.pen_up()
    self.pen_down()

