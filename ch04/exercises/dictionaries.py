article = ("Soft robotics is an emerging field where robots are made of soft, pliable materials as opposed to rigid ones. Soft growing robots can create new material and grow as they move. These machines could be used for operations in remote areas where humans can't go, such as inspecting or installing tubes underground or navigating inside the human body for biomedical applications. Current soft growing robots drag a trail of solid material behind them and can use heat and/or pressure to transform that material into a more permanent structure, much like how a 3D printer is fed solid filament to produce its shaped product. However, the trail of solid material gets more difficult to pull around bends and turns, making it hard for the robots to navigate terrain with obstacles or winding paths")


substitutions = {
  "Soft": "Moveable",
  "opposed": "rather than",
  "growing": "enlarge",
  "move": "roatate",
  "Current": "NOW",
  "pressure": "pushh",
  "transform": "Bless",
  "material": "texture",
  "printer":"machine",
  "solid":"liquid",
}

for key, value in substitutions.items():
  article = article.replace(key,value)

  print(article)

  