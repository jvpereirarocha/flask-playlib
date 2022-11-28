from sqlalchemy.orm import registry

from entities.user import User
from entities.play import Play
from adapters.orms.user import users_table
from adapters.orms.play import games_table

mapper_registry = registry()

def start_mappers():
    print(f"initializing mappers...", end="\n")
    mapper_registry.map_imperatively(
        User,
        users_table,
        properties={
            "id": users_table.c.user_id,
            "name": users_table.c.name,
            "email": users_table.c.email,
            "password": users_table.c.password,
        },
    )
    mapper_registry.map_imperatively(
        Play,
        games_table,
        properties={
            "id": games_table.c.play_id,
            "name": games_table.c.name,
            "category": games_table.c.category,
            "console": games_table.c.console,
        },
    )