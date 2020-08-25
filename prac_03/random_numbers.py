import random

RANDOM_NUMBERS = 15

out_file = open("temps_input.txt", 'w')
for i in range(RANDOM_NUMBERS):
    number = random.uniform(-200, 200)
    print("{:.2f}".format(number), file=out_file)
out_file.close()
