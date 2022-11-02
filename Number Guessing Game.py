import random

highest_number = input("What do you want your highest number to be?: ")

if highest_number.isdigit():
    highest_number = int(highest_number)
    if highest_number <= 0:
        print("Type a number higher than zero next time.")
        quit()

else:
    print ("Please type a number next time.")
    quit()

random_number = random.randint(0,highest_number)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please type a number next time. ')
        continue
    
    if user_guess == random_number:
        print("You got it! ")
        break
    else:
        if user_guess > random_number:
            print("You were above the number! ")
        else:
            print("You were below the number! ")
        
        
print("You got it in", guesses, "guesses")

    
