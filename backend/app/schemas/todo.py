# backend/app/schemas/todo.py
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class TagBase(BaseModel):
    """タグの基本スキーマ"""
    name: str = Field(..., min_length=1, max_length=100, description="タグ名")
    color: str = Field(default="#3B82F6", pattern="^#[0-9A-Fa-f]{6}$", description="タグの色（HEX）")

class TagCreate(TagBase):
    """タグ作成用スキーマ"""
    pass

class TagResponse(TagBase):
    """タグレスポンス用スキーマ"""
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True

class TodoBase(BaseModel):
    """Todoの基本スキーマ"""
    title: str = Field(..., min_length=1, max_length=255, description="Todoのタイトル")
    description: Optional[str] = Field(None, description="Todoの説明")
    completed: bool = Field(default=False, description="完了状態")

class TodoCreate(TodoBase):
    """Todo作成用スキーマ"""
    tag_names: Optional[List[str]] = Field(default=[], description="関連付けるタグ名のリスト")

class TodoUpdate(BaseModel):
    """Todo更新用スキーマ"""
    title: Optional[str] = Field(None, min_length=1, max_length=255, description="Todoのタイトル")
    description: Optional[str] = Field(None, description="Todoの説明")
    completed: Optional[bool] = Field(None, description="完了状態")
    tag_names: Optional[List[str]] = Field(None, description="関連付けるタグ名のリスト")

class TodoResponse(TodoBase):
    """Todoレスポンス用スキーマ"""
    id: int
    tags: List[TagResponse] = Field(default=[], description="関連付けられたタグ")
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

class TodoListResponse(BaseModel):
    """Todo一覧レスポンス用スキーマ"""
    todos: List[TodoResponse]
    total: int
    completed: int
    pending: int
    
class TodoStatsResponse(BaseModel):
    """Todo統計レスポンス用スキーマ"""
    total_todos: int
    completed_todos: int
    pending_todos: int
    completion_rate: float
