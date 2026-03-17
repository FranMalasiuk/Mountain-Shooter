from Player import Player
from Enemy import Enemy
from Background import Background

class EntityFactory:
    @staticmethod
    def get_entity(entity_type: str):
        if entity_type == "player":
            return Player("Hero", "Surface", "Rect")
        elif entity_type == "enemy":
            return Enemy("Ork", "Surface", "Rect")
        elif entity_type == "background":
            return Background("Forest", "Surface", "Rect")
        return None