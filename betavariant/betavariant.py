import random

random.seed(3)

# Define the parameters
alpha = 0.9
beta = 0.1

# 1. Call the built-in random.betavariate function
#    It takes the parameters alpha and beta.
result = random.betavariate(alpha, beta)

print(result)

