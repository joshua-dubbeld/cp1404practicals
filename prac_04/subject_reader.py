"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    display_subject_details(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    data = []
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        data.append(parts)
    return data
    input_file.close()


def display_subject_details(data):
    """Get data in list form and produce details in a nicely formatted string"""
    number_of_subjects = len(data)
    for subject in range(number_of_subjects):
        subject_code = data[subject][0]
        subject_teacher = data[subject][1]
        subject_number_of_students = data[subject][2]
        print("{} is taught by {:12} and has {:3} students".format(subject_code, subject_teacher,
                                                                   subject_number_of_students))



main()
