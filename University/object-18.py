# Write a program which stores country name, population and area in 1 list and then store this list multiple times until the user enters “” in the country name. Calculate average density and print the name of the country whose population density is low.

list2 = []
denslist = []

while True:
    list1 = []
    a = input("Enter Country Name: ")
    if a == "":
        for r in range(len(list2)):
            if list2[r][3] == mindens:
                print(
                    "The country with the minimum population density is", list2[r][0])
        break
    else:
        b = int(input("Enter Country's Population: "))
        c = int(input("Enter Country's Area: "))
        dens = b/c
        list1.append(a)
        list1.append(b)
        list1.append(c)
        list1.append(dens)
        denslist.append(dens)
        list2.append(list1)
        print(list2)
        mindens = min(denslist)
