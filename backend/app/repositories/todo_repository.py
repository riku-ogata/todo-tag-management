# backend/app/repositories/todo_repository.py
from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy import and_
from ..models.todo import Todo, Tag
from ..schemas.todo import TodoCreate, TodoUpdate

class TodoRepository:
    """Todoデータアクセス層（LaravelのRepository層に相当）"""
    
    def __init__(self, db: Session):
        self.db = db
    
    def get_all(self) -> List[Todo]:
        """すべてのTodoを取得"""
        return self.db.query(Todo).all()
    
    def get_by_id(self, todo_id: int) -> Optional[Todo]:
        """IDでTodoを取得"""
        return self.db.query(Todo).filter(Todo.id == todo_id).first()
    
    def create(self, todo_data: TodoCreate) -> Todo:
        """新しいTodoを作成"""
        # タグの処理
        tags = []
        if todo_data.tag_names:
            for tag_name in todo_data.tag_names:
                tag = self.db.query(Tag).filter(Tag.name == tag_name).first()
                if tag:
                    tags.append(tag)
        
        # Todoオブジェクトを作成
        todo = Todo(
            title=todo_data.title,
            description=todo_data.description,
            completed=todo_data.completed or False
        )
        
        # タグを関連付け
        todo.tags = tags
        
        # データベースに保存
        self.db.add(todo)
        self.db.commit()
        self.db.refresh(todo)
        
        return todo
    
    def update(self, todo_id: int, todo_data: TodoUpdate) -> Optional[Todo]:
        """Todoを更新"""
        todo = self.get_by_id(todo_id)
        if not todo:
            return None
        
        # フィールドを更新
        if todo_data.title is not None:
            todo.title = todo_data.title
        if todo_data.description is not None:
            todo.description = todo_data.description
        if todo_data.completed is not None:
            todo.completed = todo_data.completed
        
        # タグの更新
        if todo_data.tag_names is not None:
            tags = []
            for tag_name in todo_data.tag_names:
                tag = self.db.query(Tag).filter(Tag.name == tag_name).first()
                if tag:
                    tags.append(tag)
            todo.tags = tags
        
        # データベースに保存
        self.db.commit()
        self.db.refresh(todo)
        
        return todo
    
    def delete(self, todo_id: int) -> bool:
        """Todoを削除"""
        todo = self.get_by_id(todo_id)
        if not todo:
            return False
        
        self.db.delete(todo)
        self.db.commit()
        return True
    
    def get_by_tag(self, tag_name: str) -> List[Todo]:
        """タグでTodoを検索"""
        return self.db.query(Todo).join(Todo.tags).filter(Tag.name == tag_name).all()
    
    def get_completed_todos(self) -> List[Todo]:
        """完了済みのTodoを取得"""
        return self.db.query(Todo).filter(Todo.completed == True).all()
    
    def get_pending_todos(self) -> List[Todo]:
        """未完了のTodoを取得"""
        return self.db.query(Todo).filter(Todo.completed == False).all()
    
    def save(self, todo: Todo) -> Todo:
        """Todoを保存"""
        self.db.commit()
        self.db.refresh(todo)
        return todo
