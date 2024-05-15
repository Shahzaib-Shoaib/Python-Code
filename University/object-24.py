# Develop a function that takes a list as a parameter and returns a list with unique values from the provided list: [1, 1, 2, 2, 2, 2, 3, 4, 4, 4, 5, 6, 6, 7]

def uniqueNumberIdentifier(list1):
    b = 0
    count = 0
    for i in range(len(list1)):
        if list1.count(list1[b]) > 1:
            list1.remove(list1[b])
            count = count + 1
        else:
            b = b+1

    print("The count of the removed values are", count)
    print(list1)


list1 = [1, 1, 2, 2, 2, 2, 3, 4, 4, 4, 5, 6, 6, 7]
uniqueNumberIdentifier(list1)
