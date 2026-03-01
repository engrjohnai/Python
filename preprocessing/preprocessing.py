

sentence = input()
sentence_split = sentence.split()
stripped_words = []

for word in sentence_split:
    cleaned_word = word.strip(",.!?")
    lowercase_word = cleaned_word.lower()
    stripped_words.append(lowercase_word)

combined_sentence = ' '.join(stripped_words)
 
print(combined_sentence)



