#link to google collab: https://colab.research.google.com/drive/1NuWuC6H7o7-UL3m0iFQF2EPWJvb0XI10?usp=sharing

import random 

number = random.randint(1,100)
guess = 0

while guess != number:

  guess = int(input("ENTER GUESS:"))

  if (guess < number):
    print("guess higher")
  elif (guess > number):
    print("guess lower")
  else:
    print("correct")