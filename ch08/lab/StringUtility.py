
class StringUtility:
  def __init__(self,string):
    self.string = string
    
  def __str__(self):
    return self.string

  def vowels(self):
    vowel = ["a","e","i","o","u"]
    for vowel in self.string:
      count = len(self.string)
      return str(count) 
      if count >= 5:
        count = print("many")
        return count 
    print(count)

  def bothEnds(self):
    for i in self.string:
      return (str[0:2] + str[-2:])
      if len((str[0:2] + str[-2:])) < 2:
        return ''
    
  def fixStart(self):
    spng = str[0] + str[1].replace(str[0],'*')
    return spng
    if self.string <= 1 :
      return ''
        
  def asciiSum(self):
    return sum(ord(self.string))
        
  def cipher(self):
    cipher = ""
    for i in self.string:
      if i.isalpha():
        alphabet = ord(i) + len(self.string)
        if alphabet > ord("z"):
          alphabet -= 26
      letter = chr(alphabet)
      cipher += letter
      return cipher
  