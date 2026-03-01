Docstring for search_string.heading

Markdown heading
Report a typo

Markdown syntax is used to format a text. To create a heading, you should add # in front of a word or phrase. The number of hash signs # corresponds to the heading level, ranging from 1 to 6:

# Heading level 1
## Heading level 2
### Heading level 3
#### Heading level 4
##### Heading level 5
###### Heading level 6

Complete the heading() function that converts a given string into a Markdown-formatted heading. The function accepts two parameters: a required string parameter for the heading text, and an optional integer parameter for the heading level (with a default value of 1).

Return a string formatted as a Markdown heading by adding the appropriate number of hash signs (#) before the text. Valid heading levels range from 1 to 6. If the specified level is less than 1, the function should default to level 1. Similarly, if the level is greater than 6, it should use level 6. Here are some examples of the expected behavior:

heading("A")      # Returns "# A"
heading("A", 3)   # Returns "### A"
heading("A", 1)   # Returns "# A"
heading("A", 0)   # Returns "# A"
heading("A", 10)  # Returns "###### A"

The function should return the formatted heading string, not print it. Do not call the function in your code.
Hint by
Temporary Pseudonym avatar
Temporary Pseudonym
If you're failing test #8, make sure you account for negative inputs. This should be clarified in the question imo.
Was this hint helpful?
Write a program in Python 3