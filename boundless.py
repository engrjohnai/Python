"""
Determine if the secret_number is infinite and save your findings in the variable check.

"""

import math

secret_number = float(input(123454552))

check = math.isfinite(secret_number)

print(check)