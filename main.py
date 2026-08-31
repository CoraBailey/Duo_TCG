from renderer import CardRenderer
from card import CharacterCard

kara = CharacterCard(
    name="Kara", 
    attack=4, 
    life=10, 
    energy=3, 
    description="A brave warrior from a distant planet with a strong sense of justice.", 
    capability="Guardian", 
    descriptor="Scientist", 
    distinction="Hero")


renderer = CardRenderer()
renderer.render_card(kara)