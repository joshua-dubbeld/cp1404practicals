"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


def main():
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))
    rating = calculate_rating(score)
    print(rating)
    random_number = generate_random_number()
    print("Random number: {}".format(random_number))
    rating = calculate_rating(random_number)
    print(rating)


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
