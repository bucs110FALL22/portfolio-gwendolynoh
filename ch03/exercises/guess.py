import random

numlist = range(1,11)

random.choice(numlist)
number = random.choice(numlist)


for i in range(3):
  print ("Guess the number between 1-10")    
  guess = int(input())
  if guess < number:
    print("Too Low")
  if guess > number:
    print("Too High")
  if guess == number:
    print("correct!!")
    