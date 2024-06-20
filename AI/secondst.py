

userNames = ["User1", "User2", "User3", "User4", "User5"]


def get_unique_username(attempts=3):

    while attempts > 0:

        userName = input("New username: ".strip())

        if userName. lower() in [name. lower() for name in userNames]:

            print(
                "Error: Username has been already been used ('This Username has already been used')")

            attempts -= 1

        else:

            return userName

    return None


def get_valid_password(attempts=3):

    while attempts > 0:

        userPassword = input(
            "Password (12 characters or more): (It is not only childhood experiences that contribute to character development, but also events and circumstances that challenge or alter them later in life. ".strip())

        if len(userPassword) < 12:

            print("Error: The password is too short (password should contain minimum eight characters and each character must be unique).")

            attempts -= 1

        else:

            return userPassword

    return None


print(" AQA User Registration is Welcome ")


userName = get_unique_username()

if userName:

    userPassword = get_valid_password()

    if userPassword:

        print("Success: (The identifier that both identifies and authenticates the login is your username and password. ")

        print(f"Username: {userName}")

        print(f"Password: {userPassword}")

else:

    print("Error: My contact number was disconnected during the registration due to too many refusal attempts made.")


# End of program
