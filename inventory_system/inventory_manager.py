from typing import List, Optional
from .item import Item

class InventoryManager:
    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols
        self.slots = [[None for _ in range(cols)] for _ in range(rows)]

    def add_item(self, item: Item) -> bool:
        """Adds an item to the first available slot."""
        for row in self.slots:
            for i, slot in enumerate(row):
                if slot is None:
                    row[i] = item
                    return True
        return False  # Inventory full

    def remove_item(self, item_id: str) -> Optional[Item]:
        """Removes an item by ID."""
        for row in self.slots:
            for i, slot in enumerate(row):
                if slot and slot.id == item_id:
                    removed_item = row[i]
                    row[i] = None
                    return removed_item
        return None  # Item not found

    def display_grid(self):
        """Display the inventory grid."""
        for row in self.slots:
            print(["Empty" if not slot else slot.name for slot in row])

    def move_item(self, from_row: int, from_col: int, to_row: int, to_col: int) -> bool:
        """Move an item from one slot to another."""
        if self.slots[from_row][from_col] and not self.slots[to_row][to_col]:
            self.slots[to_row][to_col] = self.slots[from_row][from_col]
            self.slots[from_row][from_col] = None
            return True
        return False

    def use_item(self, item_id: str, callback: Optional[callable] = None):
        item = self.remove_item(item_id)
        if item and callback:
            callback(item)
