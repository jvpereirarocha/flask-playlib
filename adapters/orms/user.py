from sqlalchemy import String, Table, Column
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import registry

mapper_registry = registry()
metadata = registry.metadata


users_table = Table(
    'users',
    metadata,
    Column('user_id', UUID, nullable=False, primary_key=True),
    Column('name', String(100), nullable=False, unique=False),
    Column('email', String(255), nullable=False, unique=True),
    Column('password', String(32), nullable=False),
)