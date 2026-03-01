

import string

username = input()

the_template = string.Template(f"Dear {username}! It was really nice to meet you. Hopefully, you have a nice day! See you soon, {username}!")

print(the_template.template)