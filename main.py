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
    
print("\nCharacters saved to database:")
print("-" * 40)

for character in db.get_characters():
    print(f"{character[0]}: {character[1]} — {character[2]} / {character[3]}")

print("-" * 40)
print(f"Total characters: {len(characters)}")