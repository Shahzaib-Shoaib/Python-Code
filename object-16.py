# Find out the factorial of a given number using while loop.

num = int(input("Enter a number: "))
factorial = 1
a = 1

while a <= num:
    factorial *= a
    a += 1

print("The factorial of", num, "is", factorial)
