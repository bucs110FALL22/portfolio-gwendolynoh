
class StringUtility:
  def __init__(self,string):
    self.string = string
    
  def __str__(self):
    return self.string

  def vowels(self):
    count = 0
    for char in self.string:
      vowel = ["a","e","i","o","u"]
      if char in vowel:
          count +=1
    if count < 5: 
      return f"{count}"
    else: 
      return "many"

  def bothEnds(self):
    size = len(self. string)
    if size > 2:
      return f"{self.string[0]}{self.string[1]}{self.string[size-2]}{self.string[size-1]}"
    else:
      return ""
    
  def fixStart(self):
    if len(self.string) >1:
      char_1 = self.string[0]
      newString = ""
      check = False
      for char in self.string: 
        if char != char_1:
          newString += char 
        else:
          if check == True:
            newString += "*"
          else:
            newString += char
            check = True 
      return newString 
    else: 
      return self.string 
           
  def asciiSum(self):
    value = 0 
    for char in self.string:
      value += ord(char)
    return value 
    return sum(ord(self.string))
        
  def cipher(self):
    alphabet =[
      "a","b","c","d","e","f","g","h","i", "j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"
    ]
    alpha = []
    for a in alphabet:
      alpha.append(a.upper())
    size = len(self.string)
    newString = ""
    for c in self.string:
      check = False
      if c == " ":
        newString += " "
        continue 
      for d in alphabet:
        if c == d: 
          check = True 
          num = alphabet.index(d)
          newNum = num + size  
          while newNum > 25:
            newNum -= 26
          newString += alphabet[newNum]
      if check == False:
        for d in alpha:
          if c == d:
            check = True 
            num = alpha.index(d)
            newNum = num + size 
            while newNum < 25:
              newNum -=26
            newString +=alpha[newNum]
    return newString 
      