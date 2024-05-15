fpath = "C:\\Users\\means\\Desktop\\Shahzaib University Assignments\\CSSE 305 Lab\\Python-Code\\Number.txt"
with open(fpath,"w") as fopen:
    for i in range (5):
        a = input("Enter any number: ")
        fopen.write(a)
        fopen.write(",")
        