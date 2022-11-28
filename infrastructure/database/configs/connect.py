import logging
from os import environ
from dotenv import load_dotenv
from infrastructure.database.configs.abstraction import AbstractDatabase

from infrastructure.database.configs.engine import SessionMixin, EngineMixin

load_dotenv()


class DatabaseConnection(AbstractDatabase, SessionMixin, EngineMixin):
    def __init__(self, url=None, **kwargs) -> None:
        self.url = url or environ.get('DATABASE_URI')
        self.kwargs = kwargs
        self.bind = self.get_engine()
        super().__init__(bind=self.bind)
        self.commited = None
        self.session = None
    
    def __enter__(self):
        self.commited = False
        if self.session is None:
            self.session = self.create_session()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
        self.session.expunge_all()

    def commit(self):
        self.session.commit()
        self.commited = True
    