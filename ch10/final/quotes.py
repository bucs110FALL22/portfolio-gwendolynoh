import requests

class Quotes:
  def __init__(self):
    self.url = "https://api.adviceslip.com/advice"
   
  def get_advice(self):   
    response = requests.get(self.url)
    advice = response.json()
    data = advice.get('slip')
    real_advice =data["advice"]
    return real_advice

