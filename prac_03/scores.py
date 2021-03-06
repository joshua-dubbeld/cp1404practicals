import random


def main():
    out_file = open("results.txt", 'w')
    number_of_scores = int(input("Number of scores: "))
    for i in range(number_of_scores):
        number = generate_random_number()
        result = calculate_rating(number)
        print("{} is {}".format(number, result), file=out_file)
    out_file.close()


def calculate_rating(score):
    if score > 90:
        return "Excellent"
    elif score > 50:
        return "Passable"
    elif score < 50:
        return "Bad"


def generate_random_number():
    number = random.randint(0, 100)
    return number


main()
