Vowels and consonants
Report a typo

Let's work with texts! You'll get a sequence of characters (a word, a sentence or just gibberish). For each character tell if it's a vowel or a consonant. If you hit a non-alphabetic symbol, just stop processing.

The input format:

One line with N characters.

We will use letters from the English alphabet. The symbols aeiou are considered vowels. Treat the rest of the letters as consonants.

The output format:

Print the line vowel if the character is a vowel, and consonant if the character is a consonant. Stop printing information at the first non-alphabetic symbol.

Consider using a string method isalpha() to discriminate between an alphabetic and a non-alphabetic symbol. This method returns True if the string contains only alphabetic characters, False otherwise. For example:

print("string".isalpha()) # True print("str!!ing".isalpha()) # False

Sample Input 1:

somegibberish

Sample Output 1:

consonant
vowel
consonant
vowel
consonant
vowel
consonant
consonant
vowel
consonant
vowel
consonant
consonant

Sample Input 2:

normal phrase

Sample Output 2:

consonant
vowel
consonant
consonant
vowel
consonant

Sample Input 3:

weusedtowritewithnospaces

Sample Output 3:

consonant
vowel
vowel
consonant
vowel
consonant
consonant
vowel
consonant
consonant
vowel
consonant
vowel
consonant
vowel
consonant
consonant
consonant
vowel
consonant
consonant
vowel
consonant
vowel
consonant

Write a program in Python 3