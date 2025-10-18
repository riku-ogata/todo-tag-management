# backend/app/routers/todos.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from ..models.todo import Todo, Tag

router = APIRouter(prefix="/todos", tags=["todos"])

@router.get("/")
async def get_todos(db: Session = Depends(get_db)):
    """Todo一覧を取得"""
    try:
        todos = db.query(Todo).all()
        result = []
        for todo in todos:
            result.append({
                "id": todo.id,
                "title": todo.title,
                "description": todo.description,
                "completed": todo.completed,
                "tags": [{"id": tag.id, "name": tag.name, "color": tag.color} for tag in todo.tags],
                "created_at": todo.created_at.isoformat() if todo.created_at else None,
                "updated_at": todo.updated_at.isoformat() if todo.updated_at else None
            })
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{todo_id}")
async def get_todo(todo_id: int, db: Session = Depends(get_db)):
    """特定のTodoを取得"""
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    
    return {
        "id": todo.id,
        "title": todo.title,
        "description": todo.description,
        "completed": todo.completed,
        "tags": [{"id": tag.id, "name": tag.name, "color": tag.color} for tag in todo.tags],
        "created_at": todo.created_at.isoformat() if todo.created_at else None,
        "updated_at": todo.updated_at.isoformat() if todo.updated_at else None
    }

@router.post("/")
async def create_todo(
    title: str,
    description: str = None,
    completed: bool = False,
    tag_names: List[str] = [],
    db: Session = Depends(get_db)
):
    """新しいTodoを作成"""
    try:
        # タグの処理
        tags = []
        for tag_name in tag_names:
            tag = db.query(Tag).filter(Tag.name == tag_name).first()
            if tag:
                tags.append(tag)
        
        # Todoオブジェクトを作成
        todo = Todo(
            title=title,
            description=description,
            completed=completed
        )
        
        # タグを関連付け
        todo.tags = tags
        
        # データベースに保存
        db.add(todo)
        db.commit()
        db.refresh(todo)
        
        return {
            "id": todo.id,
            "title": todo.title,
            "description": todo.description,
            "completed": todo.completed,
            "tags": [{"id": tag.id, "name": tag.name, "color": tag.color} for tag in todo.tags],
            "created_at": todo.created_at.isoformat() if todo.created_at else None,
            "updated_at": todo.updated_at.isoformat() if todo.updated_at else None
        }
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))