"""
CP1404 Practical
Count the number of words in a string
"""

words_dict = {}

words = input("Text: ")
word_list = words.split()
print(word_list)

for word in word_list:
    if word in words_dict:
        words_dict[word] += 1
    else:
        words_dict[word] = 1

for word in words_dict:
    print("{} : {}".format(word, words_dict[word]))
