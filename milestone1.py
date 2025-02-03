import json

def load_data(file_path):
    with open(file_path, "r") as handle:
        return json.load(handle)

def animal_reader(animal):
    name = animal["name"]
    location = ", ".join(animal["locations"])
    characteristics = animal["characteristics"]
    diet = characteristics.get("diet", "Unknown")
    animal_type = characteristics.get("type", "Unknown")
    return name, diet, location, animal_type

def string_creator(data):
    animals_string = ''
    for animal in data:
        name, diet, location, animal_type = animal_reader(animal)
        animals_string += (
            f'<li class="cards__item">\n'
            f'  <div class="card__title">{name}</div>\n'
            f'  <p class="card__text">\n'
            f'    <ul>\n'
            f'      <li>Diet: {diet}</li>\n'
            f'      <li>Location: {location}</li>\n'
            f'      <li>Type: {animal_type}</li>\n'
            f'    </ul>\n'
            f'  </p>\n'
            f'</li>\n'
        )
    return animals_string

def html_replacer(animals_data):
    with open("animals_templates.html", "r") as html_object:
        placeholder = html_object.read()

    new_content = placeholder.replace("__REPLACE_ANIMALS_INFO__", string_creator(animals_data))

    with open("animals.html", "w") as new_file:
        new_file.write(new_content)

def main():
    file_path = "animals_data.json"
    animals_data = load_data(file_path)
    html_replacer(animals_data)

if __name__ == "__main__":
    main()