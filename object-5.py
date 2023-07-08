# Object # 05: Ask the user to enter a number between 10 and 20 (inclusive). If they enter a number within the range display the message "Thank you" , otherwise display message "Incorrect answer".

a = int(input("Please enter a number between 10 and 20 (inclusive): "))

if a >= 10:
    if a <= 20 :
        print("Thank You")
    else:
        print("Incorrect answer")
else:
    print("Incorrect answer")