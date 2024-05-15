# Reverse a list in python. List can be assumed.

a = [1, 2, 3, 5, 7, 9, 6, 5, 65]
revList = []

for i in range(len(a)-1, -1, -1):
    revList.append(a[i])
    if len(revList) == len(a):
        print(revList)
