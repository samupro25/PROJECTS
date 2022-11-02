#implementation of multiple dice rolls at the same time and showing what each dice rolled individually
import random
from collections import Counter

#Welcoming the user to the game
print("Hello and welcome to the dice roller!")
name = input("What is your name?: ")
print ("Hi", name)

while True:
   #Asking the user if he wants to play to make it break the loop and say bye whenever he stops playing
   wants_to_play = input("Do you want to play? (y/n): ").lower()
   
   #if statement to determine the number of dice faces, and to "roll the dice" hypothetically.
   if wants_to_play == "y":
      die_face = int(input("Select the number of faces you want your dice to have. WARNING: if you don't select a whole number, the dice roller won't work. "))
      die_amount = int(input("Select how many dices of the given faces you want to roll: "))

      #generating dice roll number with the given input
      die_rolls = []
      for i in range(0, die_amount):
         die_rolls.append(random.randint(1,die_face))

      #counting how many of each element in the list are they
      num = Counter(die_rolls)
      percentages = sum(num.values())
      total = round(percentages, 1)


      #printing final message output to the user
      print("Your dice percentages where: ")
      for face, count in num.most_common():
         print(f"{face}: {count} ({count/total:.2%})")


   
   #When the user stops wanting to play, saying them goodbye
   else:
      print("Well, it was great while it lasted! Until next time!")
      break


print("Developed by SMB Studios")