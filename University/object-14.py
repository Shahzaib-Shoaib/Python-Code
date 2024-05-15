# Create a variable callled compnum and set the value to 50. Ask the user to enter a number. While their guess is not the same as the compnum value , tell them if their guess is too low or too high and ask them to have another guess. If they enter the same value as the compnum. Display the messsage "Welldone".

compnum = 50
a = 0

while a == 0:
    b = int(input("Enter a number: "))

    if b < compnum:
        print("Too low, try again.")
    elif b > compnum:
        print("Too high, try again.")
    else:
        print("Well done!")
        break
