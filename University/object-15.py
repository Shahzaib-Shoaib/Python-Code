# Ask the user to enter a number between 10 and 20. If they enter a value under 10, display the message "Too Low" and ask them to try again. If they enter a value above 20, display the message "Too High" and ask them to try again. Keep asking until they enter a value that is between 10 and 20, then display the message "Thank You".

a = 0

while a == 0:
    num = int(input("Enter a number between 10 and 20: "))

    if num < 10:
        print("Too low, try again.")
    elif num > 20:
        print("Too high, try again.")
    else:
        print("Thank you!")
        break
