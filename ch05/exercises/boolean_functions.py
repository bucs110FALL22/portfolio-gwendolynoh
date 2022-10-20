def percentage_to_letter(score):
  if score >= 90:
    letter = "A"
  elif 90> score >=80:
    letter = "B"
  elif 80> score >=70:
    letter = "C"
  elif 70> score >=60:
    letter = "D"
  elif 60>= score:
    letter = "F"
  return letter

def is_passing(letter):
  if letter == "A":
    return True 
  if letter == "B":
    return True 
  if letter == "C":
    return True 
  else:
    return False
  return letter in "ABC"
print(is_passing(letter))

score = int(intput(percentage_to_letter("What is your score?")))