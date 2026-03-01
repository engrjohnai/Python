
import json

iris = {}

def add_iris(
    id_n,
    species,
    petal_length,
    petal_width,
    **kwargs
):
    new_entry = {
        'species': species,
        'petal_length': petal_length,
        'petal_width': petal_width
    }

    new_entry.update(kwargs)

    iris[id_n] = new_entry
    

add_iris(0, 'Iris versicolor', 4.0, 1.3, petal_hue='pale lilac')

print(json.dumps(iris, indent=4))