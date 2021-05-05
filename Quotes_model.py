import requests
import json


class Quotes:
  def __init__(self, string):
    if string == 'random':
      self.obj = self.random_quote()
    elif string == 'today':
      self.obj = self.today_quote()
  
  def random_quote(self):
    resp = requests.get('https://zenquotes.io/api/random')
    json_data = json.loads(resp.text)
    quote = json_data[0]['q']
    author = json_data[0]['a']
    fullPhrase = f"{quote} by {author}"
    return fullPhrase

  
  def today_quote(self):
    resp = requests.get('https://zenquotes.io/api/today')
    json_data = json.loads(resp.text)
    quote = json_data[0]['q']
    author = json_data[0]['a']
    fullPhrase = f"{quote} by {author}"
    return fullPhrase
