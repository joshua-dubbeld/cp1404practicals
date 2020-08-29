
import random

MIN_VALUE = 1
MAX_VALUE = 45
QUICKPICKS_PER_LINE = 6

quick_pick_line = []

number_of_lines = int(input("How many quick picks? "))
for line in range(number_of_lines):
    for number in range(QUICKPICKS_PER_LINE):
        quickpick = random.randint(MIN_VALUE, MAX_VALUE)
        quick_pick_line.append(quickpick)
    quick_pick_line.sort()
    print(quick_pick_line)
    quick_pick_line.clear()
