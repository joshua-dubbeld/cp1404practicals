"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import os


def main():
    """Demo os module functions."""
    print("Starting directory is: {}".format(os.getcwd()))

    # Change to desired directory
    os.chdir('Lyrics/Christmas')

    # Loop through each file in the (current) directory
    for filename in os.listdir('.'):
        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue

        new_name = get_fixed_filename(filename)
        if filename == new_name:
            continue
        print("Renaming {} to {}".format(filename, new_name))
        os.rename(filename, new_name)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    new_name = ''
    for i, character in enumerate(filename):
        new_character = character
        try:
            if filename[i] == ' ':
                new_character = '_'
            elif new_name[-1] == '_':
                new_character = character.upper()
            elif character == '_':
                new_character = character
            elif filename[i + 1].isupper():
                new_character = character + '_'
        except IndexError:
            pass
        new_name += new_character

    return new_name


main()
