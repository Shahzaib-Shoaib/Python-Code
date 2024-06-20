# AQA User Registration with additional requirements

# Existing usernames list (case insensitive)
userNames = ["User1", "User2", "User3", "User4", "User5"]

def get_unique_username(attempts=3):
    while attempts > 0:
        userName = input("New username: ").strip()
        if userName.lower() in [name.lower() for name in userNames]:
            print("Error: The username has been used before.")
            attempts -= 1
        else:
            return userName
    return None

def get_valid_password(attempts=3):
    while attempts > 0:
        userPassword = input("Password (12 characters or more): ").strip()
        if len(userPassword) < 12:
            print("Error: The password is too short.")
            attempts -= 1
        else:
            return userPassword
    return None

print("Welcome to AQA User Registration")

# Get a unique username with limited attempts
userName = get_unique_username()
if userName:
    # Get a valid password with limited attempts
    userPassword = get_valid_password()
    if userPassword:
        print("Success: Your username and password are valid.")
        print(f"Username: {userName}")
        print(f"Password: {userPassword}")
else:
    print("Error: Registration failed due to too many invalid attempts.")

# End of program
