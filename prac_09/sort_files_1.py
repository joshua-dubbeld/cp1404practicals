import os

extensions = []

os.chdir("FilesToSort")

for filename in os.listdir('.'):
    extension_index = filename.find('.')
    extension = filename[extension_index + 1:]
    if extension not in extensions:
        extensions.append(extension)
    try:
        os.mkdir(extension)
    except FileExistsError:
        print("'{}' directory already exists.".format(extension))
print(extensions)
