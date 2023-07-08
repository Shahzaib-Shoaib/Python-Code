# Turn every item of a list into its square in python. List can be assumed.

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sqList = []
for i in range(len(a)):
    sqList.append(a[i]**2)

    if (len(sqList) == len(a)):
        print(sqList)
