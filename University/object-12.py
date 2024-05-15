# Ask how many people the user want to invite to a party. If they enter a number below 10, ask for the names and after each name, display "[name] has been invited". If they enter a number which is 10 or higher , display the message "Too many people"

a = int(input("How many people do you want to invite to a party? "))

if a < 10:
 for i in range(a):
        name = input("Enter the name of guest : ")
        print(name,"has been invited")
else:
    print("Too many people")

