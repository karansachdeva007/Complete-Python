# Write a program that asks the user to input a number and prints whether the number is positive and even, positive and odd, or negative.

num = int(input("Enter a number: "))

if num > 0:
    if num % 2 == 0:
        print("The number is positive and even.")
    else:
        print("The number is positive and odd.")
else:
    print("The number is negative.")
