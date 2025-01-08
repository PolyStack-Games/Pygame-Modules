import pygame
from .inventory_manager import InventoryManager
from .item import Item

class InventoryUI:
    def __init__(self, inventory: InventoryManager, slot_size: int = 50, spacing: int = 5):
        self.inventory = inventory
        self.slot_size = slot_size
        self.spacing = spacing
        self.font = pygame.font.Font(None, 24)

    def draw(self, screen: pygame.Surface, x: int, y: int):
        """Draws the inventory grid."""
        for row_idx, row in enumerate(self.inventory.slots):
            for col_idx, item in enumerate(row):
                slot_x = x + col_idx * (self.slot_size + self.spacing)
                slot_y = y + row_idx * (self.slot_size + self.spacing)
                pygame.draw.rect(
                    screen,
                    (200, 200, 200),
                    (slot_x, slot_y, self.slot_size, self.slot_size),
                    1
                )
                if item:
                    # Draw item icon or placeholder
                    text_surface = self.font.render(item.name, True, (255, 255, 255))
                    screen.blit(text_surface, (slot_x + 5, slot_y + 5))

    def draw_tooltip(self, screen: pygame.Surface, item: Item, x: int, y: int):
        if not item:
            return
        text_surface = self.font.render(item.name, True, (255, 255, 255))
        screen.blit(text_surface, (x, y))