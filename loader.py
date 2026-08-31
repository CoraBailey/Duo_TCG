import json

from card import CharacterCard

def load_characters(json_file):
    with open(json_file, "r") as file:
        character_data = json.load(file)

    characters = []

    for data in character_data:
        character = CharacterCard(
            name=data["name"],
            attack=data["attack"],
            life=data["life"],
            energy=data["energy"],
            description=data["description"],
            capability=data["capability"],
            descriptor=data["descriptor"],
            distinction=data["distinction"],
            ability=data["ability"]
        )

        characters.append(character)

    return characters