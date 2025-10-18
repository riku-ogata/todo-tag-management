# backend/app/models/todo.py
from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from datetime import datetime

Base = declarative_base()

# 多対多関係のための関連テーブル
todo_tags = Table(
    'todo_tags',
    Base.metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('todo_id', Integer, ForeignKey('todos.id', ondelete='CASCADE'), nullable=False),
    Column('tag_id', Integer, ForeignKey('tags.id', ondelete='CASCADE'), nullable=False),
    Column('created_at', DateTime, default=func.now()),
)

class Tag(Base):
    __tablename__ = 'tags'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False, unique=True)
    color = Column(String(7), default='#3B82F6')
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    
    # リレーションシップ
    todos = relationship("Todo", secondary=todo_tags, back_populates="tags")

class Todo(Base):
    __tablename__ = 'todos'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    description = Column(Text)
    completed = Column(Boolean, default=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    
    # リレーションシップ
    tags = relationship("Tag", secondary=todo_tags, back_populates="todos")
