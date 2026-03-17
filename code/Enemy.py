from Entity import Entity

class Enemy(Entity):
    def move(self) -> None:
        print(f"Inimigo {self.name} patrulhando.")