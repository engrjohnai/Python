

text = input()
words = text.split()

if not words:
    print("")
else:
    result = words[0]
    for word in words[1:]:
        result += word.capitalize()
    print(result)