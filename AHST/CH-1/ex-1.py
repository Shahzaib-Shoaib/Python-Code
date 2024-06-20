# ##########################
# # AQA User Registration #
# ##########################
userNames = ["User1", "User2", "User3", "User4", "User5"]
print("Welcome to AQA User Registration")


userName = input("New username: ")

if userName in userNames:
    print("Error")
    
else:

    userPassword = input("Password (12 characters or more): ")

    if len(userPassword)>=12:
        print(userName)
        print(userPassword)
    
        
# # end of program
