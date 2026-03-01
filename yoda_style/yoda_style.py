
import random

sentence = input()

split_sentence = sentence.split()
random.seed(43)
random.shuffle(split_sentence)

rejoin = ' '.join(split_sentence)

print(rejoin)