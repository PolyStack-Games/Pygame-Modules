class Item:
    def __init__(self, id: str, name: str, description: str, icon_path: str, stack_size: int = 1):
        self.id = id
        self.name = name
        self.description = description
        self.icon_path = icon_path
        self.stack_size = stack_size

    def __repr__(self) -> str:
        return f"Item(id={self.id}, name={self.name}, stack_size={self.stack_size})"
