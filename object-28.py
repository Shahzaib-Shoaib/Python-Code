# Create a new file. Ask the user  to enter 1, 2 or 3, if they select anything other than 1, 2 or 3, it should display the error message. If they select 1, ask the user to enter a school subject and save it to a new file called “Subject.txt”. It should overwrite any existing file with a new file. If they select 2, display the contents of the “Subject.txt” file. If they select 3, ask the user to enter a new subject and save it to the file and display the entire contents of the file.

a = input("Enter 1, 2 or 3: ")
fpath = "C:\\Users\\means\\Desktop\\Shahzaib University Assignments\\CSSE 305 Lab\\Code\\Subjects.txt"

if a == "1":
    b = input("Enter Subject: ")
    with open(fpath, "w") as f:
        f.write(b)


elif a == "2":
    # Using a+ instead of r to prevent error if the file is not available
    with open(fpath, "a+") as f:
        x = f.read()
    print(x)

elif a == "3":
    c = input("Enter Subject: ")

    with open(fpath, "a") as f:
        f.write("\n")
        f.write(c)
    with open(fpath, "r") as f:
        y = f.read()
    print(y)

else:
    print("Error Message")
