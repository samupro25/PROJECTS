import random

name =input("What is your name: ")
print ("Hello,",name)

#elements used to generate the password
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbol = "[]{}#;._-()/"

#joining all of the elements 
all=lower + upper + number + symbol

#inputing the user's length of password
length = input("Select your password length: ")

#generating the password with the selected length and the "all" variable
password = "".join(random.sample(all,int(length)))
print(name,", the password generated for you is :",password)