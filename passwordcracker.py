import random
import time

password = input("Type your password here: ")
length = int(input("Type the length of your password here: "))
correctpass = False
pswrdguess = ("")
guesses = 0
st = time.time()

lower = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")
upper = ("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z")
number = ("0","1","2","3","4","5","6","7","8","9",)
symbol = ("!","$","%","/","(",")","=","?","¿","*",":","_",";","@","#","[","]","{","}",".","",",","+","¡")
characters = lower



while correctpass == False:

   if pswrdguess != password:
      pswrdguessprocess = random.sample(characters, length)
      pswrdguess = "".join(pswrdguessprocess)
      correctpass = False
      guesses += 1

   else: 
      correctpass = True

et = time.time()
elapsed_time = et - st

print("Your password is:", pswrdguess)
print("Your password was cracked in:", guesses, "guesses.")
print('Execution time:', elapsed_time, 'seconds')