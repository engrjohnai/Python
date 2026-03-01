
def tallest_people(**names):
    max_height = max(names.values())
    
    tallest_names = []
    for name, height in names.items():
        if height == max_height:
            tallest_names.append(name)
    
    tallest_names.sort()

    
    for name in tallest_names:
        print(f"{name} : {max_height}")

tallest_people(Jackie=176, Wilson=185, Saersha=165, Roman=185, Abram=169)