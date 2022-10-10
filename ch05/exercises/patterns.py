def star_pyramin():
  print("How many number of rows?")
  stars = int(input(":"))
  for i in range(stars):
    print("*" * (i + 1))
    

star_pyramin()

def rstar_pyramind():
  print("How many number of rows?")
  stars = int(input(":"))
  for i in reversed(range(stars)):
    print("*" * (i + 1))
rstar_pyramind()