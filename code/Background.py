from Entity import Entity

class Background(Entity):
    def move(self) -> None:
        print(f"Background {self.name} rolando.")