print("Press 1 to add a name to the list")
print("Press 2 to change the name in the list")
print("Press 3 to delete a name from the list")
print("Press 4 to display whole list")
print("Press 5 to end the program")
list1 = []

while True:
    a = input("Enter any number to perform operation: ")
    if a == "1":
        b = input("Enter the name you want to add to the list: ")
        list1.append(b)
    elif a == "2":
        c = input("Enter the name you want to change in the list: ")
        for i in range(len(list1)):
            if (c == list1[i]):
                d = input("Enter New Name : ")
                list1[i] = d
    elif a == "3":
        e = input("Enter the name you want to delete from the list: ")
        for r in range(len(list1)):
            if (e == list1[r]):
                list1.remove(e)
    elif a == "4":
        print(list1)
    elif a == "5":
        break
    else:
        print("Enter a number according to the above table")
