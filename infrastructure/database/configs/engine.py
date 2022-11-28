import os
from abc import ABC
from typing import Optional
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


class EngineMixin:
    def __init__(self, **kwargs) -> None:
        self.kwargs = kwargs
    
    def get_engine(self):
        
        engine = create_engine(
            url=self.url,
            **self.kwargs
        )
        return engine


class SessionMixin:
    def __init__(self, bind, auto_commit: bool = False, auto_flush: bool = True, expire_on_commit: bool = False):
        self.bind = bind
        self.auto_commit = auto_commit
        self.auto_flush = auto_flush
        self.expire_on_commit = expire_on_commit
    
    def create_session(self):
        session = Session(bind=self.bind, autocommit=self.auto_commit, autoflush=self.auto_flush, expire_on_commit=self.expire_on_commit)
        return session