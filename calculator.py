'''Credit to Samuel Molero Badia for this calculator build as a project'''
print("Hello, and welcome to a simple python calculator!")
print("Take into account that this is only a two number calculator and that it has it's limits. Don't try to do advanced algebra because it won't work.")


operation = input("What kind of operation would you like to do. (+,:,*,-) ")
number1 = int(input("What do you want your first number to be?: "))
number2 = int(input("What do you want your second number to be?: "))


def multiplication(number1, number2):
    answer = number1 * number2
    print("Your answer is: ", answer)


def division(number1, number2):
    answer = number1 / number2
    print("Your answer is: ", answer)


def substraction(number1, number2):
    answer = number1 - number2
    print("Your answer is: ", answer)


def adding(number1, number2):
    answer = number1 + number2
    print("Your answer is: ", answer)


if operation == "+":
    adding(number1, number2)
elif operation == "*":
    multiplication(number1, number2)
elif operation == ":":
    division(number1, number2)
elif operation == "-":
    substraction(number1, number2)
else:
    print("The input you gave is not valid, try repeating it again.")
