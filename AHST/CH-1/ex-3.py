

##########################
# AQA User Registration #
##########################


userNames = list(map(str.lower, ["User1", "User2", "User3", "User4", "User5"]))
passw= False

print("Welcome to AQA User Registration")
i = 0 
while i < 3:
    userName = input("New username: ").lower()

    if userName in userNames:
        print("Error")
        i = i +1
        if i == 3:
            print("Only 3 allowed")
            
        
    else:
        passw = True
        break
r = 0
if passw == True:
    
    while r< 3:
    
        userPassword = input("Password (12 characters or more): ")

        if len(userPassword)>=12:
            print("Your username is " + userName)
            print("Your password is " + userPassword)
            break
        else:
            print("Password should be longer")
            r=r+1
            if r == 3:
                print("Only 3 allowed")
            
        
        
# end of program
