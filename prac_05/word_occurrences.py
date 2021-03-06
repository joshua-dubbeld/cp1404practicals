"""
CP1404 Practical
Count the number of words in a string
"""

words_dict = {}

largest_word_length = 0

text = input("Text: ")
words = text.split()

for word in words:
    if word in words_dict:
        words_dict[word] += 1
    else:
        words_dict[word] = 1

    if len(word) > largest_word_length:
        largest_word_length = len(word)


for word in sorted(words_dict):
    print("{:{}} : {}".format(word, largest_word_length, words_dict[word]))
