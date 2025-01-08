import json

def save_inventory(self, filepath: str):
    with open(filepath, 'w') as file:
        json.dump([[item.id if item else None for item in row] for row in self.slots], file)

def load_inventory(self, filepath: str, item_map: dict):
    with open(filepath, 'r') as file:
        data = json.load(file)
        for row_idx, row in enumerate(data):
            for col_idx, item_id in enumerate(row):
                self.slots[row_idx][col_idx] = item_map.get(item_id)
