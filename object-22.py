# Remove the empty strings from the list of strings in python. List can be assumed.

list1 = ["Hi", "Ziti", "", "Babuska", "Minmin", "Fester", "", "Soup", ""]
list2 = []

for r in range(len(list1)):
    if list1[r] != "":
        list2.append(list1[r])
print(list2)
