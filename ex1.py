'''

Exercise 1
Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they will turn 100 years old.

Extras:

Add on to the previous program by asking the user for another number and printing out that many copies of the previous message.
(Hint: order of operations exists in Python)
Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)

'''

# Create a program that asks the user to enter their name and their age.
name = input("What is your name? ")

# to correct this to ensure it is an integer.
# see https://www.w3schools.com/python/python_try_except.asp
try:
    age = int(input("What is your age? "))
    numberOfTimes = int(input("How many times do you want me to tell you? "))
except ValueError as error:
    print("Invalid Age - we are going to treat you like a five year old")
    age = 5
    numberOfTimes = 1

if age <= 100:
    years = 100 - age
    message = f", you will turn 100 in {years} years"
else:
    years = age - 100
    message = f", you turned 100  {years} years ago"

#Print out a message addressed to them that tells them the year that they will turn 100 years old.
for i in range (numberOfTimes):
    print(f"{i}: Hi {name}, you are {age} years old{message} ")
    # print("Hi "+ name +", you are "+ age +" years old" +message)

#Print out a message addressed to them that tells them the year that they will turn 100 years old.

print(f"Hi {name}, you are {age} years old{message} \n"* numberOfTimes)