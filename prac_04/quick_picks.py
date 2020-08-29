
import random

MIN_VALUE = 1
MAX_VALUE = 45
QUICKPICKS_PER_LINE = 6

quick_pick_line = []
used_quickpick_numbers = []

number_of_lines = int(input("How many quick picks? "))
for line in range(number_of_lines):
    for number in range(QUICKPICKS_PER_LINE):
        quickpick = random.randint(MIN_VALUE, MAX_VALUE)

        # Checks if the generated quick pick has already been used. If it has, it generates a new one.
        while quickpick in used_quickpick_numbers:
            quickpick = random.randint(MIN_VALUE, MAX_VALUE)

        quick_pick_line.append(quickpick)
        used_quickpick_numbers.append(quickpick)

    quick_pick_line.sort()
    for number in range(len(quick_pick_line)):
        print("{:3}".format(quick_pick_line[number]), end="")
    print()

    # Clears lists for next line
    quick_pick_line.clear()
    used_quickpick_numbers.clear()
