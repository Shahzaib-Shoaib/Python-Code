# a = 1
# total = 0
# incr = 0
# while (a == 1):
# 	b = int(input('Enter Positive Numbers: '))
# 	if(b>=0):
# 		total = total +b
# 		incr= incr + 1
# 	else:
# 		print("Total is", total)
# 		print("Count is", incr)
# 		break

# Write a python program that keeps taking numbers from the user until presses enter-key without typing a number; in such case, your program should print sum and count of the positive numbers entered by the user.

# a = 1
# total = 0
# incr = 0
# while (a == 1):
#     b = (input('Enter Numbers: '))
#     if (b == ""):
#         print("The total is", total)
#         print("Count of positive number is", incr)
#         break
#     else:
#         b = int(b)
#         if (b > 0):
#             incr = incr + 1
#             total = total + b
#         else:
#             total = total + b

##################################################################3

# a = 1
# sum = 0
# countn = 0
# counta = 0
# while (a == 1):
#     b = (input('Enter Numbers: '))
#     if (b == ""):
#         print("The sum of all positive numbers are", sum)
#         print("Count of negative numbers are", countn)
#         print("Count of all input values (Zeroes ignored) are", counta)
#         break
#     else:
#         b = int(b)
#         if (b > 0):
#             sum = sum + b
#             counta = counta + 1
#         elif (b < 0):
#             countn = countn + 1
#             counta = counta + 1
#         else:
#             print("Ignore")



##################################################################3


# n = int(input("Enter the value of n: "))
# pc = 0
# nc = 0

# for i in range(n):
#     num = int(input("Enter a number: "))
#     if num > 0:
#         pc = pc + 1
#     elif num < 0:
#         nc = nc + 1

# print("Count of positive numbers :", pc)
# print("Count of negative numbers :", nc)
