Write a function that searches for an object with a specific memory address characteristic. 
The function should iterate through integers from 0 to 10,000, checking each number's memory address using the id() function. 
The goal is to find the first integer whose memory address ends with the digits '888'.

To check if a memory address ends with '888', use the modulo operator (%) to examine the last three digits (e.g., 54321 % 1000 = 321).

Return the first integer that satisfies this condition.