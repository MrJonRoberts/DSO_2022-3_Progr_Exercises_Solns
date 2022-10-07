'''
Exercise 2
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
 Hint: how does an even / odd number react differently when divided by 2?
 Extras:

If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
'''
for i in range(10):
    try:
        number = int(input("Enter a number: "))
        check = int(input("Enter check number: "))
    except ValueError:
        print("Not a number")

    if check == 0:
        check = 2

    if number % check == 0:
        print(f"{number} is divisible by {check}")
    else:
        print(f"{number} is not divisible by {check}")