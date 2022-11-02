import random

status = "red"
combination = random.randint(1, 100)
guess = 0

while status == "red":
   guess += 1
   if guess == combination:
      status = "green"

print("Congratulations, the correct combination was: ", guess)