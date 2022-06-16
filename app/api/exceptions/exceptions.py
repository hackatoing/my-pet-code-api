class ItemNotFound(Exception):
    def __init__(self, name: str):
        self.name = name
        self.msg = f"{self.name} not found"
