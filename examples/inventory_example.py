from pygame_core import Game, create_game_context, Scene, Settings

from inventory_system.inventory_manager import InventoryManager
from inventory_system.item import Item
from inventory_system.ui import InventoryUI


class Setting(Settings):
    """A class to store all settings for the Snake game."""

    colors: dict = {
        "background": (0, 0, 0),
        "text": (255, 255, 255)
    }

class Inventory(Scene):
    """
    The Inventory scene displays the player's inventory.

    Attributes:
        screen (pygame.Surface): The main game screen.
        game_context (GameContext): The game context.
    """

    def __init__(self, screen, context):
        super().__init__(screen, context)
        self.inventory = InventoryManager(5, 3)
        self.ui = InventoryUI(self.inventory)

        self.inventory.add_item(Item("potion", "Potion", "Restores health", "potion.png"))
        self.inventory.add_item(Item("sword", "Sword", "A sharp blade", "sword.png"))
        self.inventory.add_item(Item("shield", "Shield", "Protects from damage", "shield.png"))
        self.inventory.add_item(Item("key", "Key", "Opens locked doors", "key.png"))

    def update(self, input_manager):
        pass

    def render(self):
        self.ui.draw(self.screen, 50, 50)

if __name__ == "__main__":
    import pygame
    # pylint: disable=no-member
    pygame.init()
    # pylint: enable=no-member

    screen = pygame.display.set_mode((1920, 1080))
    pygame.display.set_caption("Inventory Example")

    game_context = create_game_context(None, Setting())

    game_context.scene_manager.set_initial_scene(Inventory(screen, game_context))
    game = Game(screen)
    game.run(game_context.scene_manager)
    # pylint: disable=no-member
    pygame.quit()
    # pylint: enable=no-member
