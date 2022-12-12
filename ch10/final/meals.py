import requests
from pprint import pprint as pp

class Meals:
  def __init__(self):
    self.url = "http://www.themealdb.com/api/json/v1/1/random.php?"

  def get_meal(self):
    r = requests.get(self.url)
    responce = r.json()
    meal = responce.get("meals")[0]
    instructions = str(meal["strInstructions"])
    garb = "\r\n"
    while garb in instructions:
      instructions = instructions.replace(garb, '')
    return instructions

