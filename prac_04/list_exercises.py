
number_of_numbers = int(input("How many numbers? "))
total = 0
numbers = []
for i in range(number_of_numbers):
    number = int(input("Number: "))
    numbers.append(number)
    total += number

average = total / number_of_numbers
print("The first number is {}".format(numbers[0]))
print("The last number is {}".format(numbers[-1]))
print("The smallest number is {}".format(min(numbers)))
print("The largest number is {}".format(max(numbers)))
print("The average of the numbers is {:.2f}".format(average))


