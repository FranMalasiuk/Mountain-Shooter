from Menu import Menu
from Level import Level

class Game:
    def __init__(self):
        self.window = "Screen_Surface"
        self.menu = Menu(self.window)
        # O diagrama indica 1..* (uma ou mais fases)
        self.levels = [Level(self.window, "Fase 01")]

    def run(self) -> None:
        self.menu.run()
        for lvl in self.levels:
            lvl.run()

if __name__ == "__main__":
    game = Game()
    game.run()