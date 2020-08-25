MIN_LENGTH = 8

password = input("Password: ")
while len(password) < MIN_LENGTH:
    print("Password needs to be {} characters long!".format(MIN_LENGTH))
    password = input("Password: ")

print("Your password is: ")
for char in password:
    print("*", end="")
