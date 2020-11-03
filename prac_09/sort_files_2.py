import os

extensions = []
extension_categories = {}

os.chdir("FilesToSort")

for filename in os.listdir('.'):
    extension_index = filename.find('.')
    extension = filename[extension_index + 1:]
    if extension not in extensions:
        extensions.append(extension)
        category = input("What category would you like to sort {} files into? ".format(extension))
        extension_categories[extension] = category
    try:
        os.mkdir(extension)
    except FileExistsError:
        pass
print(extension_categories)
