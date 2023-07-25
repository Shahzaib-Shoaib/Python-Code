import csv
fpath = "C:\\Users\\means\\Desktop\\Shahzaib University Assignments\\CSSE 305 Lab\\Python-Code\\GradingRules.txt"
gradeAndPoint = []
with open(fpath, "r") as f:
    while True:
        list1 = []
        content = f.readline()
        if content != "":
            split = content.split(",")

            list1.append(split)
            gradeAndPoint.append(list1)
        else:
            break
data = []
headerLine = ["S.No", "Seat Number", "Name",
              "Father Name", "Theory Marks", "Lab Marks", "Total", "Marks In Words", "Alphabetic Grade"]
x = 0
while True:
    a = input("Enter Seat Number:")
    if a != "":
        recordList = []
        x = x+1
        b = input("Enter Name:")
        c = input("Enter Father's Name:")
        d = int(input("Enter Marks in Theory:"))
        e = int(input("Enter Marks in Lab:"))
        f = d+e
        recordList.append(x)
        recordList.append(a)
        recordList.append(b)
        recordList.append(c)
        recordList.append(str(d))
        recordList.append(str(e))
        recordList.append(f)
        for i in range(len(gradeAndPoint)):
            if gradeAndPoint[i][0][0] == str(f):
                numberalpha = gradeAndPoint[i][0][1]
                alphagrade = gradeAndPoint[i][0][2]
                recordList.append(numberalpha)
                recordList.append(alphagrade)

        data.append(recordList)
        print(recordList)

    else:
        break

with open("forSemesterCell.csv", "w", encoding="UTF8", newline="") as ft:
    writer = csv.writer(ft)
    writer.writerow(headerLine)
    writer.writerows(data)
