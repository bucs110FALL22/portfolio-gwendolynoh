class Rectangle:
  def __init__(self, x, y, h, w):
    '''
Function sets the instance variables x,y, height, and width of the rectangle so that the values cannot be lower than 0. 

    '''
    self.x = max(0,x)
    self.y = max(0,y) 
    self.height = max(0,h)
    self.width = max(0,w)
    
  def __str__(self):
    '''
The function uses f-strings to return strings of x,y,height, and width but does not print the values 
    '''
    str_result = f" x:{self.x}, y:{self.y}"
    str_result += f" \nheight:{self.height}"
    str_result += f" \nwidth:{self.width}"
    return str_result
  
