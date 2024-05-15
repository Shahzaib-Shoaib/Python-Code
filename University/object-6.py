# Object # 06: Ask the user's age, if they are 18 or over , display the message "You can vote". If they are aged 17 , display the message "You can learn to drive". If they are aged 16, display the message "You can buy a lottery ticket". If they are under 16 , display the message "You can go Trick or Treating".

age = int(input("What is your age? "))

if age >= 18:
    print("You can vote.")
elif age == 17:
    print("You can learn to drive.")
elif age == 16:
    print("You can buy a lottery ticket.")
else:
    print("You can go Trick or Treating.")