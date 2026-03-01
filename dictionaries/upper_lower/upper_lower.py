


words = input()

words_lower = words.lower().split()
words_upper = words.upper().split()

word_dict = dict(zip(words_upper, words_lower))
print(word_dict)

