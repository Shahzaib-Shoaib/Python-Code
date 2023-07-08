# Develop a student grading system according to the following instructions:
# 1. Take input of five subjects obtained marks
# 2. Sum up the marks
# 3. Grade the marks as below:
# (i) : If obtained marks are => 90 and < 101 Grade A+
# (ii) : If obtained marks are => 80 and < 90 Grade A
# (iii) : If obtained marks are => 70 and < 80 Grade B

com = float(input("Enter Computer Marks: "))
phy = float(input("Enter Physics Marks: "))
eng = float(input("Enter English Marks: "))
isl = float(input("Enter Islamiat Marks: "))
urd = float(input("Enter Urdu Marks: "))

obt = com + phy + eng + isl + urd

per = (obt / 425) * 100
print(per,"%")

if per>100:
    print("Invalid Percentage")
elif per >= 90 and per <=100:
    print("Grade A+")
elif per < 90 and per >=80:
    print("Grade A")
elif per < 80 and per >=70:
    print("Grade B")
elif per < 70 and per >=60:
    print("Grade C")
elif per < 60 and per >=50:
    print("Grade D")
else:
    print("Failed")


