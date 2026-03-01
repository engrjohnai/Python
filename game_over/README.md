Game over
Report a typo

In online test games, there is usually a limited number of lives: if, for example, you make 3 mistakes, you lose, and cannot continue with the game. Let's try to implement this system.


Read the line with user answers from the input: C for a correct answer and I for an incorrect one, separated by space. The objective is to count the final score, which is the number of correct answers. Count them until the user reaches 3 incorrect answers. If they make no more than 2 mistakes, they win. In this case print "You won" and their score, otherwise print "Game over" along with their score. Display the message and score on separate lines, without quotation marks.

The input format:

A line with N user answers in a game separated by space

The output format:

Game over or You won
Final score

Sample Input 1:

C C C I C C C C I I C C C C C C C C C

Sample Output 1:

Game over
7

Sample Input 2:

C C I I C C C C C C C C C C C

Sample Output 2:

You won
13