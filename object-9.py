# Ask the user to enter a number between 1 and 12 and then display the times table for that number.

a = int(input("Enter any number: "))

for i in range(1, 13):
    print(a,"x",i,"=",a*i)