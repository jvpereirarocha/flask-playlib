from sqlalchemy import String, Table, Column
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import registry

metadata = registry.metadata


games_table = Table(
    'games',
    metadata,
    Column('play_id', UUID, nullable=False, primary_key=True),
    Column('name', String(255), nullable=False, unique=False),
    Column('category', String(100), nullable=False, unique=False),
    Column('console', String(32), nullable=False),
)