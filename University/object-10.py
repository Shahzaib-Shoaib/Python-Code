# Ask for a number below 50 and then count down from 50 to that number, making sure you show the number they entered in the output.

a = int(input("Enter a number below 50: "))

if (a < 50):
    for i in range (50, a-1, -1):
        print(i)
else:
    print("Number is not less than 50")