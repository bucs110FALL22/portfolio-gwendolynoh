class Rectangle:
  def __init__(self,x,y,height,width):
    self.x = x
    self.y = y   
    self.height = height
    self.width = width

  def __str__(self):
    result = f" x is {self.x}, y is {self.y}, height is {self.height}, width is {self.width}"
    return(result)
  
    