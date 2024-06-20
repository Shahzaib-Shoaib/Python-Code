
##########################
# AQA User Registration #
##########################
userNames = ["User1", "User2", "User3", "User4", "User5"]
print("Welcome to AQA User Registration")
userName = input("New username: ")
if userName in userNames:
    print("The username is already used")
else:
    userPassword = input("Password (12 characters or more): ")
    if len(userPassword) >= 12:
        print("The password is not long enough")
    else:
        print("Your username is " + userName)
        print("Your password is " + userPassword)
# end of program


