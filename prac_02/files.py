# # 1.
# name = input("Name: ")
# out_file = open("name.txt", 'w')
# print(name, file=out_file)
# out_file.close()

# # 2.
# in_file = open("name.txt", 'r')
# print("Your name is {}".format(in_file.read()))

# # 3.
# in_file = open("numbers.txt", 'r')
# numbers = in_file.readlines()
# total = int(numbers[0].strip('\n')) + int(numbers[1].strip('\n'))
# print(total)
# in_file.close()

# # 4.
# total = 0
# in_file = open("numbers.txt", 'r')
# for line in in_file:
#     total += int(line.strip('\n'))
#
# print(total)
# in_file.close()
