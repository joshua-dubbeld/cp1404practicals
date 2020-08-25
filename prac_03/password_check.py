MIN_LENGTH = 8


def main():
    password = get_password()
    print_asterisks(password)


def print_asterisks(password):
    print("Your password is: ")
    for char in password:
        print("*", end="")


def get_password():
    password = input("Password: ")
    while len(password) < MIN_LENGTH:
        print("Password needs to be {} characters long!".format(MIN_LENGTH))
        password = input("Password: ")
    return password


main()
