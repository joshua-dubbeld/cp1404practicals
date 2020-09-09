"""
CP1404 Practical
Hex colours in a dictionary
"""

hex_colours_dict = {"aliceblue": "#f0f8ff", "antiquewhite": "#faebd7", "aquamarine1": "#7fffd4", "azure1": "#f0ffff",
                    "beige": "#f5f5dc", "black": "#000000", "blanchedalmond": "#ffebcd", "blue1": "#0000ff",
                    "blueviolet": "#8a2be2", "brown": "#a52a2a"}

colour_name = input("Enter colour: ").lower()
while colour_name != "":
    if colour_name in hex_colours_dict:
        print(hex_colours_dict[colour_name])
    else:
        print("Invalid colour name")
    colour_name = input("Enter colour: ").lower()
