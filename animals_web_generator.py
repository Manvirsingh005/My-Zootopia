import json


def load_data(file_path):
    """Load JSON data from a file."""
    with open(file_path, "r") as handle:
        return json.load(handle)


def serialize_animal(animal_obj):
    """Serialize a single animal object into an HTML card."""
    characteristics = animal_obj.get("characteristics", {})
    name = animal_obj.get("name", "")
    diet = characteristics.get("diet", "")
    location = characteristics.get("locations", [""])[0]
    animal_type = characteristics.get("type", "")

    output = '<li class="cards__item">\n'
    output += f'  <div class="card__title">{name}</div>\n'
    output += '  <div class="card__text">\n'
    output += '    <ul>\n'
    if diet:
        output += f'      <li><strong>Diet:</strong> {diet}</li>\n'
    if location:
        output += f'      <li><strong>Location:</strong> {location}</li>\n'
    if animal_type:
        output += f'      <li><strong>Type:</strong> {animal_type}</li>\n'
    output += '    </ul>\n'
    output += '  </div>\n'
    output += '</li>\n'
    return output


def serialize_animals(data):
    """Serialize all animals into an HTML cards list."""
    output = ""
    for animal in data:
        output += serialize_animal(animal)
    return output


def create_html(data, template_file, output_file):
    """Read the template, insert animal data, and write final HTML."""
    with open(template_file, "r") as handle:
        html_template = handle.read()

    animals_html = serialize_animals(data)

    final_html = html_template.replace("__REPLACE_ANIMALS_INFO__", animals_html)

    with open(output_file, "w") as handle:
        handle.write(final_html)


if __name__ == "__main__":
    data = load_data("animals_data.json")  # load data
    create_html(data, "animals_template.html", "animals.html")  # create final html
