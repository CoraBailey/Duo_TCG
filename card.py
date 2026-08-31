class Card:
    def __init__(self, name: str, description: str = ""):
        self.name = name
        self.description = description

class CharacterCard(Card):
    def __init__(self, name: str, attack: int = 0, life: int = 0, energy: int = 0, description: str = "", capability: str = "", descriptor: str = "", distinction: str = "", ability: str = "", card_type: str = "Character"):
        super().__init__(name, description)
        self.attack = attack
        self.life = life
        self.energy = energy
        self.capability = capability
        self.descriptor = descriptor
        self.distinction = distinction
        self.ability = ability
        self.card_type = card_type
    
    def __str__(self):
        return (
            f"{self.name}\n"
            f"{self.capability} | {self.descriptor} | {self.distinction}\n"
            f"Energy: {self.energy}\n"
            f"Attack: {self.attack}\n"
            f"Life: {self.life}\n"
            f"{self.description}"
        )
    

class AttackCard(Card):
    def __init__(self, name: str, description: str = "", damage: int = 0, card_type: str = "Attack"):
        super().__init__(name, description)
        self.damage = damage
        self.card_type = card_type

    def __str__(self):
        return (
            f"{self.name}\n"
            f"Damage: {self.damage}\n"
            f"{self.description}"
        )

class ReactionCard(Card):
    def __init__(self, name: str, description: str = "", defense: int = 0, effect: str = "", card_type: str = "Reaction"):
        super().__init__(name, description)
        self.defense = defense
        self.effect = effect
        self.card_type = card_type

    def __str__(self):
        return (
            f"{self.name}\n"
            f"Defense: {self.defense}\n"
            f"Effect: {self.effect}\n"
            f"{self.description}"
        )