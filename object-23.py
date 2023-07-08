# Remove all occurrences of the same item from the list of strings in python. List is  [5, 20, 15, 20, 25, 50, 20]

list1 = [5, 20, 15, 20, 25, 50, 20]
b = 0

for i in range(len(list1)):
    if list1.count(list1[b]) > 1:
        list1.remove(list1[b])
    else:
        b = b + 1

print(list1)
