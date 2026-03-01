text = "ice cream"
print(text)
print(text[0:3])
print(text[4:9])
print(text[4:])
print(text[:-1])
statement = "Earth revolves around the sun"
print(statement[6:14])
print(statement[-3:])


s='maine 200 banana khaye'
s=s.replace('banana','samosa')
s=s.replace('200','10')
print("Using two line replace:",s)

s='maine 200 banana khaye'
s=s.replace('banana','samosa').replace('200','10')
print("Using single line:",s)
