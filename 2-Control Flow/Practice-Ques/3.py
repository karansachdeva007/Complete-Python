# Write a program that asks the user to input a number and prints whether the number is positive, negative, or zero

num = int(input("Enter a number: "))

if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
