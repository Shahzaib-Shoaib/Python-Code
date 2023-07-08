# Write a program that takes input from the user and find that number from the list along with its index number

a = [1.2, 3.0, 4.2, 6.1, 5.3, 7.4, 9.9, 8.5]
c = True
d = "Number not found"

while c:
    e = 0
    b = float(input("Enter any number: "))
    for r in range(len(a)):
        if a[r] == b:
            print("Number found at Index:", r)
            c = False
            d = ""
    print(d)
