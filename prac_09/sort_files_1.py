import os

os.chdir("FilesToSort")

for filename in os.listdir('.'):
    extension_index = filename.find('.')
    extension = filename[extension_index + 1:]
    print(extension)