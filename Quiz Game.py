print("Welcome to my computer hardware quiz!")
correct_answers = 0
playing = input("Do you want to play my quiz? ").lower()
total_answers = 4


if playing != "yes":
   quit()

print ("Okay! Let's play the game!")   

answer1 = input("What does cpu stand for: ").lower()


if answer1 == "central processing unit":
    print("Your answer is correct")
    correct_answers += 1

else:
    print("Your answer is incorrect")
    correct_answers -= 1


answer2 = input("What is the name ofthe instructions that tell the computer what to do and how to do it: ").lower()

if answer2 == "software":
    print("Your answer is correct")
    correct_answers += 1

else:
    print("Your answer is incorrect")
    correct_answers -= 1


answer3 = input("RAM stands for: ").lower()

if answer3 == "random acces memory":
    print("Your answer is correct")
    correct_answers += 1

else:
    print("Your answer is incorrect")
    correct_answers -= 1


answer4 = input("When you save a file, it is permanently saved on the: ").lower()

if answer4 == "hard drive":
    print("Your answer is correct")
    correct_answers += 1

else:
    print("Your answer is incorrect")
    correct_answers -= 1



print ("You got ", correct_answers ," out of " , total_answers, "correct answers.")
print ("Your score is: " + str((correct_answers/total_answers)*100) + "%.")    