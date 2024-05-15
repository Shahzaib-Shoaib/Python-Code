# Object # 07: Ask the user to enter 1,2 or 3. If they enter 1, display the message "Thank You". If they enter 2, display "Well done". If they enter 3 display "Correct". If they enter anything else, display "Error Message"


a = int(input("Please enter 1, 2, or 3: "))

if a == 1:
    print("Thank you")
elif a == 2:
    print("Well done")
elif a == 3:
    print("Correct")
else:
    print("Error message")
