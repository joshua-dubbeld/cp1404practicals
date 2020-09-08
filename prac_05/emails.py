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
    if choice.lower() == 'y':
        emails_dict[email] = name
    else:
        name = input("Name: ").title()
        emails_dict[email] = name

    email = input("Email: ")

print(emails_dict)
