from renderer import CardRenderer
from loader import load_characters
from db import Database

db = Database()
renderer = CardRenderer()
db.create_tables()

characters = load_characters("Duo_TCG/data/characters.json")

for character in characters:
    renderer.render_card(character)
    db.save_character(character)
    
print(db.get_characters())