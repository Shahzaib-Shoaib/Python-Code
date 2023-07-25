# Using the song "3 green bottles", display the lines "There are [num] green bottles hanging on the wall". Then ask the question "How many bottles are hanging on the wall ?". If the user answers correctly , display the message "There will be [num] green bottles hanging on the wall". If they answer incorrectly , display the message "No try again" until they get it right. When the number of green bottles gets down to (Zero), display the message "There are no more green bottles hanging on the wall".
b = 0
a = 10
print("There are", a, "green bottles hanging on the wall")
while b == 0:
    c = int(input("How many green bottles will be hanging on the wall? "))
    if (c == a):
        print("Correct")
        break
    else:
        if (a == 0):
            print("There are no more green bottles left")
            break
        else:
            print("No, Try again")
            a = a - 1
