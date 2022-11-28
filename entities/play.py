from uuid import uuid4

class Play:
    def __init__(self, name: str, category: str, console: str) -> None:
        self.play_id = uuid4().hex
        self.name = name
        self.category = category
        self.console = console

    def __str__(self) -> str:
        return f"{self.name.capitalize()}"