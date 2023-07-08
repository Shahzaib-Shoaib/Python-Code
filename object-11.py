# Set a variable called total to 0. Ask the user to enter five numbers and after each input ask them if they want that number included, if they do, then add the number to the total , if they do not want it included , do not add it to the total. After they have entered all five numbers, dispay the total.

total = 0

for i in range(5):
    n = float(input("Enter a number: "))
    a = input("Do you want this number to be included in total: ").lower()
    if a == "yes":
        total = total + n

print("Total = ", total)
