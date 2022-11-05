from Rectangle import Rectangle 

class Surface:
  def __init__(self,filename,x, y, h, w):
    '''
Function takes the parameter x,y,height, and width and creates and object that is then stored in self.rect. Filename is stored in the instance variable self.image
    '''
    self.image = filename
    self.rect = Rectangle(x, y, h, w)
    
  def getRect(self):
    '''
    Function returns retangle object 
    '''
    return self.rect
