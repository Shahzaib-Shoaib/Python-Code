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

# 3

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


# 3


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

############################################################################################

# data = [9, 25, 12, 19, 15]
# n = 5

# for i in range(0, n-2):
#     temp = data[i]
#     index = i - 1
#     while (data[index] > temp) and (index >= 0):
#         data[index+1] = data[index]
#         index = index-1
#     data[index+1] = temp

# print(temp)
# print(data)


# numhash = hash(("dfs","sdgf","dsgfg"))
# print(numhash)


# def f(x):
#     return x*x-x


# sp = -2.3
# while True:
#     sp = sp + 0.1
#     fun = f(sp)
#     print(fun, "if value of x is", sp)

#     if sp >= 3.5:
#         break
# Example dictionary
# from typing import List
# my_dict = {"name": "John", "age": 30, "city": "New York"}

# # Getting all the keys using the keys() method
# keys_list = list(my_dict.keys())  # Convert the keys view to a list (optional)
# print(keys_list)


# sample_dict = {1: 'Coffee', 2: 'Tea', 3: 'Juice'}
# for x in sample_dict:
#     print(x)


# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         sumNumbers = []
#         total = 0
#         for i in range(len(nums)):
#             for x in range(len(nums)):
#                 if (i == x):
#                     continue
#                 else:
#                     total = nums[i] + nums[x]
#                     if (target == total):
#                         if (len(sumNumbers) < 1):
#                             sumNumbers.append(i)
#                             sumNumbers.append(x)

#         return sumNumbers


# solution_instance = Solution()

# print(solution_instance.twoSum([3, 2, 4], 6)
#       )


# class Solution:
#     def firstUniqChar(self, s: str) -> int:
#         list = []
#         if (len(s) == 1):
#             answer = 0
#             return answer

#         for i in range(len(s)):
#             for x in range(len(s)):
#                 if (i == x):
#                     continue
#                 else:
#                     if (s[i] == s[x]):
#                         pass

#                     else:
#                         list.append(i)
#         for v in range(len(list)):
#             if (list.count(list[v])+1 == len(s)):
#                 answer = list[v]
#                 return answer

#         return -1

class Solution:
    def firstUniqChar(self, s: str) -> int:
        indices = []
        
        for i in range(len(s)):
            is_duplicate = False
            for x in range(len(s)):
                if i != x and s[i] == s[x]:
                    is_duplicate = True
                    break
            
            if not is_duplicate:
                indices.append(i)
        print(indices)

        for v in range(len(indices)):
            if s.count(s[indices[v]]) == 1:
                return indices[v]

        return -1  # No unique character found

# Creating an instance of the class
sol = Solution()

# Calling the method on the instance
result = sol.firstUniqChar("leetcode")
print(result)



