Yoda style
Report a typo

Everybody wants to speak like master Yoda sometimes. Create a program that transforms a given sentence into Yoda-style speech by randomly rearranging its words. Follow these steps:

    Accept a sentence as input from the user.

    Convert the input sentence into a list of words using the string.split() method.

    Set the random seed to 43 using random.seed(43). This ensures reproducibility of the random shuffle.

    Rearrange the order of words in the list and convert the shuffled list of words back into a sentence using ' '.join().

    Print the resulting Yoda-style sentence.

Notes:

    You have to use random.seed(43) before shuffling to ensure consistent results.

    The output should be a single line of text with the words in a new, randomized order.

    Preserve the original capitalization and punctuation of the words.

Sample Input 1:

Luke, I'm your father

Sample Output 1:

your father I'm Luke,

Sample Input 2:

I will be back

Sample Output 2:

be back will I