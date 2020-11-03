import os
import shutil

os.chdir("FilesToSort")


def main():
    extensions = []
    extension_categories = {}

    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue
        extension_index = filename.find('.')
        extension = filename[extension_index + 1:]
        if extension not in extensions:
            extensions.append(extension)
            category = input("What category would you like to sort {} files into? ".format(extension)).title()
            extension_categories[extension] = category
        try:
            os.mkdir(extension_categories[extension])
        except FileExistsError:
            pass
        shutil.move(filename, extension_categories[extension])


def remove_directories():
    for directory in os.listdir('.'):
        if os.path.isdir(directory):
            os.rmdir(directory)


# remove_directories()
main()
