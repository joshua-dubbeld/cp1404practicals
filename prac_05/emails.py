"""
CP1404 Practical
Store names from email input in dictionary
"""

emails_dict = {}

email = input("Email: ")
while email != "":
    email_alias = email.split('@')
    name_list = email_alias[0].split('.')
    name = ' '.join([word for word in name_list]).title()
    choice = input("Is your name {}? (Y/n) ".format(name))
    while choice.lower() not in "yn":
        print("Invalid choice.")
        choice = input("Is your name {}? (Y/n) ".format(name))
    if choice.lower() == 'y':
        emails_dict[email] = name
    elif choice.lower() == 'n':
        name = input("Name: ").title()
        emails_dict[email] = name
    else:
        print("Something went wrong...")

    email = input("Email: ")

print()
for word in emails_dict:
    print("{} ({})".format(emails_dict[word], word))
