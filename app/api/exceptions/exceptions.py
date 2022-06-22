from fastapi import HTTPException


class ItemNotFound(HTTPException):
    def __init__(self, name: str):
        self.status_code = 404
        self.name = name
        self.detail = f"{self.name} not found"


class EmptyList(HTTPException):
    def __init__(self, name: str):
        self.status_code = 404
        self.name = name
        self.detail = f"{self.name} is empty"
