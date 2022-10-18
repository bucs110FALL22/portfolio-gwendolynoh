import pygame 


#Part A 
x = 101
def indefinite_interation(x):
  num = [x]
  while (x != 1):
    if x % 2 == 0:
      x = x//2
    else:
      x = (3 * x) + 1 
    num.append(x)
  return num
print(indefinite_interation(x)) 

# Part B 
x = 101
def indefinite_interation(x):
  count = 0 
  iters = {}
  num = [x]
  while (x != 1):
    if x % 2 == 0:
      x = x//2
    else:
      x = (3 * x) + 1 
    count = count + 1 
    iters [x] = count
    print("Count is:",iters [x])
    num.append(x)
  return num
print(indefinite_interation(x)) 

upper_limit = 20
list = []
for start in range(2,upper_limit + 1):
  count = 0
  while (x != 1):
    if x % 2 == 0:
      x = x//2
    else:
      x = (3 * x) + 1 
    count = count + 1
    d = {x : count}
    list.append(d)
print (list) 

# Part C
pygame.display.init()
window = pygame.display.set_mode()

#Font on display 
pygame.font.init()
font = pygame.font.Font(None,50)

# Variables 
upper_limits = 20 
iters = {}
max_so_far = 0 
max_val = 0
scale = 5

for start in range(2,upper_limit + 1):
  window.fill("black")
  count = 0
  while (x != 1):
    if x % 2 == 0:
      x = x//2
    else:
      x = (3 * x) + 1
    count = count + 1
    d = {x : count}
    iters.item(d)
    start.append(x)
    
coords = [indefinite_interation(x),count]
pygame.draw.lines(window, "white", False, coords)
new_display = pygame.transfor.flip(window, False, True)
pygame.display.blit(new_display, (0,0))
window.display.flip()
