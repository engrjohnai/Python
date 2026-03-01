

text = input()
words = text.split()
findings = ["www.", "https://", "http://"]

for word in words:
    word_lower = word.lower()
    
    if any(word_lower.startswith(prefix) for prefix in findings):
        print(word)


