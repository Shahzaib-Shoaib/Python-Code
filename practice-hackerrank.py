# import math
# import os
# import random
# import re
# import sys


# if __name__ == '__main__':
#     n = int(input().strip())
#     print(n)
#     if n % 2 != 0:
#         print("Wierd")
#     elif n % 2 == 0 and n >= 2 and n <= 5:
#         print("Not Wierd")
#     elif n % 2 == 0 and n >= 6 and n <= 20:
#         print("Wierd")
#     elif n % 2 == 0 and n > 20:
#         print("Not Wierd")

# if __name__ == '__main__':
#     n = int(input())
#     for i in range(n):
#         print(i**2)


# def is_leap(year):
#     leap = False

#     # Write your logic here
#     if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
#         leap = True

#     return leap


# year = int(input())
# print(is_leap(year))
# if __name__ == '__main__':
#     n = int(input())
#     for i in range(n):
#         print(i+1,end="")


# if __name__ == '__main__':
#     x = int(input())
#     y = int(input())
#     z = int(input())
#     n = int(input())
#     list = []

#     newlist = []
#     list.append(x)
#     list.append(y)
#     list.append(z)
#     for i in range(x + 1):
#         for j in range(y + 1):
#             for k in range(z + 1):
#                 if i + j + k != n:
#                         newlist.append([i,j,k])

#     print(newlist)


# if __name__ == '__main__':
#     n = int(input())
#     arr = map(int, input().split())
#     arr_list = list(arr)
#     sorted_list = sorted(arr_list, reverse=True)
#     for i in range(len(sorted_list)):
#         if (sorted_list[i] < max(sorted_list)):
#             second = sorted_list[i]
#             print(second)
#             break


# if __name__ == '__main__':
#     main_list = []
#     scores_list = []
#     for _ in range(int(input())):
#         sec_list = []
#         name = input()
#         score = float(input())
#         sec_list.append(name)
#         sec_list.append(score)
#         main_list.append(sec_list)
#         scores_list.append(score)
#     sorted_score_list = sorted(scores_list)
#     main_list.sort()
#     for i in range(len(sorted_score_list)):
#         if (sorted_score_list[i] > min(sorted_score_list)):
#             second = sorted_score_list[i]
#             break
#     for x in range(len(main_list)):
#         if main_list[x][1] == second:
#             print(main_list[x][0])


# if __name__ == '__main__':
#     n = int(input())
#     student_marks = {}
#     for _ in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks[name] = scores
#     query_name = input()
#     if query_name in student_marks:
#         scores = student_marks[query_name]
#         average_score = sum(scores) / len(scores)
#         formatted_average = "{:.2f}".format(average_score)

#         print(formatted_average)


# if __name__ == '__main__':
#     arr = []
#     N = int(input())
#     for r in range(N):
#         command = input().split()
#         # Check if the command is "insert" and has two integer arguments
#         if command[0] == "insert" and len(command) == 3:
#             i = int(command[1])
#             e = int(command[2])
#             arr.insert(i, e)
#         elif (command[0] == "print" and len(command) == 1):
#             print(arr)
#         elif (command[0] == "remove" and len(command) == 2):
#             e = int(command[1])
#             arr.remove(e)
#         elif (command[0] == "append" and len(command) == 2):
#             e = int(command[1])
#             arr.append(e)
#         elif (command[0] == "sort" and len(command) == 1):
#             arr.sort()
#         elif (command[0] == "pop" and len(command) == 1):
#             arr.pop()
#         elif (command[0] == "reverse" and len(command) == 1):
#             arr.reverse()


# if __name__ == '__main__':
#     n = int(input())
#     integer_list = map(int, input().split())
#     conv_integer_tuple = tuple(integer_list)
#     print(hash(conv_integer_tuple))


# if __name__ == '__main__':
#     s = input()

#     for r in range(len(s)):

#         if s[r].isalnum() == True:
#             answer = True
#             break

#         else:
#             answer = False
#     print(answer)
#     for r in range(len(s)):

#         if s[r].isalpha() == True:
#             answer = True
#             break

#         else:
#             answer = False
#     print(answer)
#     for r in range(len(s)):

#         if s[r].isdigit() == True:
#             answer = True
#             break

#         else:
#             answer = False
#     print(answer)

#     for r in range(len(s)):

#         if s[r].islower() == True:
#             answer = True
#             break

#         else:
#             answer = False
#     print(answer)

#     for r in range(len(s)):

#         if s[r].isupper() == True:
#             answer = True
#             break

#         else:
#             answer = False
#     print(answer)

# def swap_case(s):
#     n = ""
#     for r in range(len(s)):
#         if (s[r].isalpha() == True):
#             if (s[r].islower()):
#                 n = n + s[r].upper()
#             else:
#                 n = n + s[r].lower()
#         else:
#             n = n + s[r]

#     return n


# if __name__ == '__main__':
#     s = input()
#     result = swap_case(s)
#     print(result)


# def split_and_join(line):
#     mod = line.split()
#     n = ""
#     # write your code here
#     for i in range(len(mod)):
#         n = n + "-"+mod[i]
#     return n[1:]


# if __name__ == '__main__':
#     line = input()
#     result = split_and_join(line)
#     print(result)

# def print_full_name(first, last):
#     print (f"Hello {first} {last}! You just delved into python.")
#     # Write your code here

# if __name__ == '__main__':
#     first_name = input()
#     last_name = input()
#     print_full_name(first_name, last_name)

# def mutate_string(string, position, character):
#     l = list(string)
#     l[position] = character
#     new_string = ''.join(l)
#     return new_string

# if __name__ == '__main__':
#     s = input()
#     i, c = input().split()
#     s_new = mutate_string(s, int(i), c)
#     print(s_new)

# def count_substring(string, sub_string):
#     same = []
#     another = []
#     count = 0
#     for r in range(len(string)):
#         for i in range(len(sub_string)):
#             if (string[r] == sub_string[i]):
#                 same.append(string[r])
#     for v in range(len(same)):
#         if (another.count(same[v]) < 1):
#             another.append(same[v])
#     count = len(another)

#     return count


# if __name__ == '__main__':
#     # string = "zaianb"
#     # sub_string = "rm"
#     string = input().strip()
#     sub_string = input().strip()
    

#     count = count_substring(string, sub_string)
#     print(count)


# def count_substring(string, sub_string):
#     occurrences = string.count(sub_string)
#     return occurrences

# if __name__ == '__main__':
#     string = input().strip()
#     sub_string = input().strip()
    
#     count = count_substring(string, sub_string)
#     print(count)


# def count_substring(string, sub_string):
#     c = 0
#     for i in range(len(string)):
#         s = string[i:i + len(sub_string)]
#         print(s)
#         if s == sub_string:
#             c += 1
#     return c
    
# if __name__ == '__main__':
#     string = input().strip()
#     sub_string = input().strip()
    
#     count = count_substring(string, sub_string)
#     print(count)