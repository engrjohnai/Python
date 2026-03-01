Preprocessing
Report a typo

Preprocess the input text as follows:

    Remove punctuation characters (commas, periods, exclamation marks, and question marks: ,.!?)

    Convert all characters to lowercase

Then print the processed text.

Note: Punctuation characters may appear anywhere in the input string, not just at the end. You can remove them using the following method: str.replace("!", ""). Replacing a character with an empty string effectively removes it.

Sample Input 1:

Nobody expects the Spanish inquisition! And you?!

Sample Output 1:

nobody expects the spanish inquisition and you