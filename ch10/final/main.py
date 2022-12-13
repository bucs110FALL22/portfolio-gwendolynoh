import os
from meals import Meals
from quotes import Quotes
from pprint import pprint as pp

def main():
  '''
  Imports both API's from their Class and defines both classes which are then called
  '''
  print("Here is your random recipe for the day. Hope you enjoy!!")
  recipes = Meals()
  pp(recipes.get_meal())

  print("Here is your advice for the day:")
  
  ad = Quotes()
  pp(ad.get_advice())


main()


