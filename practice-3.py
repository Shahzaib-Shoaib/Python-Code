a = int(input("Enter Number: "))
b = int(input("Enter Number: "))
s = a
if b < s:
    s = b
d = 1
print(d)
d = d+1
r1 = a % d
print("r1",r1)
r2 = b % d
print("r2",r2)

if (r1 != 0):
    d = d+1
if (r2 != 0):
    d = d+1
if (d < s):
    print(d)
