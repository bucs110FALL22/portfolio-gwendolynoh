def percentage_to_letter(score = 0):
    if score >= 90:
      return True 
    elif score <= 90 and score >= 80:
      return True
    elif score <= 80 and score >=70:
      return True 
    elif score <=70 and score >=60:
      return True 
    elif score <60:
      return True 
score = int(input("What is your score?:"))
print(percentage_to_letter(score))

#A = score >= 90
#B = score <= 90 or score >= 80
#C = score <= 80 or score >=70
#D = score <=70 or score >=60
#F = score <60

def is_passing(letter=None):
  return percentage_to_letter(score)
  if letter == A: 
    print("You passed")
    return letter 
  if letter == B: 
    print("You passed")
    return letter 
  if letter == C: 
    print("You passed")
    return letter
  if letter == D:
    print("You failed")
    return letter 
  if letter == F: 
    print("You failed")
    return letter
letter = percentage_to_letter(score)
print(is_passing(letter))
