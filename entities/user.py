class User:
    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password

    def __str__(self) -> str:
        return f"User: {self.username}"