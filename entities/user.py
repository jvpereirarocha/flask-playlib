from uuid import uuid4


class User:
    def __init__(self, name: str, email: str, password: str) -> None:
        self.user_id = uuid4().hex
        self.name = name
        self.email = email
        self.password = password

    def __str__(self) -> str:
        return f"User: {self.username}"