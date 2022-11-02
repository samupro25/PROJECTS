#original idea: https://www.youtube.com/c/TechWithTim

#asking about user data to reffer to them later on and to see if they are old enough to play the game.
print ("Welcome to my first game!")
name = input("What is your name? ")
age = int(input("What is your age? "))

#greeting the user and setting a health variable to which we will refer later on
print("Hello", name, "you are", age,"years old.")

health = 10

#checking that the user is old enough to play and asking him if he actually wants to play.
if age >= 18:
    print("You are old enough to play!")
    wants_to_play = input("Do you want to play? ").lower()
    if wants_to_play == "yes":
        print("Let's Play")
        
        #showing the health so the user knows how much health he has got so later on when health is taken out from him he can be aware
        print("You are starting with ", health, "health")
        
        #first choice, using the .lower() to make sure that the choice is correctly written and the if statement is correctly executed. 
        #Adding the extra (left/right) information at the end so the player is sure of what to write beneath.
        left_or_right = input("First choice... Left or Right (left/right)? ").lower()
        if left_or_right == "left":
            ans = input("You succesfully followed the path and ended up in a lake. Do you swim across or do you go around? (across/around) ").lower()
            if ans == "around":
                print("You went around the lake and reached the other side of the lake easily.")

              #showing that his decision was correct but taking some health out of him because of an inconvinience. 
              # taking the health out of the variable so the program has it into account for future occasions  
            elif ans == "across":
                print("You managed to get across the lake, but you where bit by a fish and lost 5 health.")
                health -= 5
            
            #making the player loose if non of the possible options where written
            else:
                print("You lost.")
            
            
            ans = input("You notice a house and a river. Which do you go? (house/river)").lower()
            if ans == "house":
                #this option's result depends on your previous decisions that's why the health was taken out from the variable before.
                print ("You go to the house and you are greeted by the owner, he doesn't like you and he punches you in the face... You lose 5 health. ")
                health -= 5

                if health <= 0:
                    print("You now have 0 health and you lost the game...")
                
                #finishing the story, announcing the player won and finally including the credits
                else:
                    print("You continue the path handling the pain and arrive to the treasure chest.")
                    print("YOU WON!")
                    print("Treasure Quest: Developed by: Samuel Molero Badia")
                
            

            else: 
                print ("You fall in the river and you drown")
        
        else: 
            print("You find a Goblin band and eventhough you tried to fight you got killed. ")
            

    else:
        print ("Have a Good Day!")

#alternative option for people younger than 18 to play but only under the supervision of an adult. Same code, only differs from the first three lines asking if they are being supervised.
elif age >= 14: 
    print ("You can play but only supervised by an adult ")
    are_you_being_supervised = input(name + ", are you being supervised by an adult?").lower()
    if are_you_being_supervised  == "yes":
        wants_to_play = input("Do you want to play? ").lower()
    if wants_to_play == "yes":
        print("Let's Play")
        print("You are starting with ", health, "health")
        left_or_right = input("First choice... Left or Right (left/right)? ").lower()
        if left_or_right == "left":
            ans = input("You succesfully followed the path and ended up in a lake. Do you swim across or do you go around? (across/around) ").lower()
            if ans == "around":
                print("You went around the lake and reached the other side of the lake easily.")

            elif ans == "across":
                print("You managed to get across the lake, but you where bit by a fish and lost 5 health.")
                health -= 5
            
            else:
                print("You lost.")
            
            
            ans = input("You notice a house and a river. Which do you go? (house/river)").lower()
            if ans == "house":
                print ("You go to the house and you are greeted by the owner, he doesn't like you and he punches you in the face... You lose 5 health. ")
                health -= 5

                if health <= 0:
                    print("You now have 0 health and you lost the game...")

                else:
                    print("You continue the path handling the pain and arrive to the treasure chest.")
                    print("YOU WON!")
                    print("Treasure Quest: Developed by: Samuel Molero Badia")
                
            

            else: 
                print ("You fall in the river and you drown")
        
        else: 
            print("You find a Goblin band and eventhough you tried to fight you got killed. ")
    else:
        print ("Have a Good Day!")
     
else: 
    print("You are not old enough to play the game...")