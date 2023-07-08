# Write a program which takes input of Student Name, Seat Number and three marks and add data to another file.
fpath = "C:\\Users\\means\\Desktop\\Shahzaib University Assignments\\CSSE 305 Lab\\Code\\data.txt"
op = open(fpath, "w")

while True:
    x = input("Enter Student's Name: ")
    if x == "":
        break
    else:
        b = input("Enter Student's Seat Number: ")
        m1 = input("Enter marks of first subject: ")
        m2 = input("Enter marks of second subject: ")
        m3 = input("Enter marks of third subject: ")
        f = open(fpath, "a")
        f.write(x)
        f.write("\t")
        f.write(b)
        f.write("\t")
        f.write(m1)
        f.write("\t")
        f.write(m2)
        f.write("\t")
        f.write(m3)
        f.write("\n")
