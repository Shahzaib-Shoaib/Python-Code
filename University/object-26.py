# a: Write a program to print smallest number in a given list and its location (index)
# b: Extend the program to interchange (swap) the first number and the location at which smallest value is found
# c: Write a python program to sort the given list of numbers by using selection sort algorithm

list1 = [23, 42, 424, 213, 76, 12, 9, 54, 35]
min = list1[0]

for i in range(len(list1)):
    if list1[i] < min:
        min = list1[i]

a = list1.index(min)
print("The minimum value", min, "is found at index number", a)

# Afer Swaping

list1[a] = list1[0]
list1[0] = min

print("List after swapping is: ", list1)

# Sorting with Selection sort algorithm


def selectionSort(lst):

    for i in range(len(lst)):
        min_index = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j

        lst[i], lst[min_index] = lst[min_index], lst[i]

    return lst


sortedList = selectionSort(list1)
print("Sorted List: ", sortedList)
