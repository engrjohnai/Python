

words = input()
vowels = {'a', 'e', 'i', 'o', 'u'}

for char in words:
    lower_char = char.lower()
    
    if not lower_char.isalpha():
        break
        
    if lower_char in vowels:
        print("vowel")
    else:
        print("consonant")

        

    
