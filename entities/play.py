class Play:
    def __init__(self, name: str, category: str, console: str) -> None:
        self.name = name
        self.category = category
        self.console = console

    def __str__(self) -> str:
        return f"{self.name.capitalize()}"