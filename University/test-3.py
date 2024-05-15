import random
print("Press 1 to perform addition")
print("Press 2 to perform subtraction")
a = input("Enter 1 or 2: ")

if a == "1":
    rnum1 = random.randint(5, 20)
    rnum2 = random.randint(5, 20)
    num1 = rnum1 + rnum2
    x = input("Guess the number: ")
    if x == num1:
        print("Congratulations! You guessed it correctly.")
    else:
        print("Incorrect Answer")
        print("The correct answer is", num1)

elif a == "2":
    rnum3 = random.randint(20, 25)
    rnum4 = random.randint(1, 25)
    num2 = rnum3 - rnum4
    y = input("Guess the number: ")
    if y == num2:
        print("Congratulations! You guessed it correctly.")
    else:
        print("Incorrect Answer")
        print("The correct answer is", num2)

else:
    print("Invalid choice!")
