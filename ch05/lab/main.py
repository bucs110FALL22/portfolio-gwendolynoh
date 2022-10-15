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
screen_width = 500
screen_height = 500
window = pygame.display.set_mode([screen_width,screen_height])


font = pygame.font.Font(None,50)
upper_limits = 20 
iters = {}
max_so_far = 0 
max_val = 
scale = 5

for start in range(2,upper_limit + 1):
  count = 0
  while (x != 1):
    if x % 2 == 0:
      x = x//2
    else:
      x = (3 * x) + 1 
    count = count + 1