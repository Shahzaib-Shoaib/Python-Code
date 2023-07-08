# a: Using the Books.csv file, ask the user how many records they want to add to the list and then allow them to add that many.
# b: You must import the csv library by using import csv.
# c: After all data has been added, ask for an author and display all the books in the list by that author. If there are no books written by that author in the list, display a message.

import csv
headerLine = ["S.No", "Book Name", "Author Name", "Year Released"]
data = []

b = int(input("How many books do you want to add: "))
x = 0

for r in range(b):
    x = x+1
    c = input("Enter Book Number: ")
    d = input("Enter Author Number: ")
    e = input("Enter year of release: ")
    recordList = []
    recordList.append(x)
    recordList.append(c)
    recordList.append(d)
    recordList.append(e)
    data.append(recordList)

fpath = "C:\\Users\\means\\Desktop\\Shahzaib University Assignments\\CSSE 305 Lab\\Code\\Books.csv"

with open("Books.csv", "w", encoding="UTF8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(headerLine)
    writer.writerows(data)

s = input("Search for an author: ")
fn = open(fpath, "r")
count = 0
while True:
    content = fn.readline()
    if content != "":
        split = content.split(",")
        if s == split[2]:
            print(split[1])
            count += 1
    else:
        break

if count == 0:
    print("Sorry, no such book found written by", s, ".")
