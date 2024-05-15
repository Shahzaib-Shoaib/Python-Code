# Ask the user to enter a number and then enter another number. Add these two numbers together and then ask if they want to add anther number. If they enter "y" ask them to enter another number and keep adding numbers until they do not answer "y". Once the loop has stopped, display the output.

a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))

total = a + b
t = 0


while(t==0):
    n = int(input("Enter any number: "))
    o = input("Do you want to add this number? ")

    if(o == "y"):
        total = total + n
    else:
        print("Total is", total)
        break
