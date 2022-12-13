import requests
from pprint import pprint as pp

class Meals:
  def __init__(self):
    self.url = "http://www.themealdb.com/api/json/v1/1/random.php?"

  def get_meal(self):
    '''
    Uses API to get random recipe. Also scraps '\r\n' in the dictionary because was written into the document. Then returns information pulled from dictionary
    '''
    r = requests.get(self.url)
    responce = r.json()
    meal = responce.get("meals")[0]
    instructions = str(meal["strInstructions"])
    garb = "\r\n"
    while garb in instructions:
      instructions = instructions.replace(garb, '')
    return instructions

