# backend/app/services/todo_service.py
from typing import List, Optional
from ..models.todo import Todo, Tag
from ..schemas.todo import TodoCreate, TodoUpdate, TodoResponse
from ..repositories.todo_repository import TodoRepository

class TodoService:
    """Todoビジネスロジック層（LaravelのService層に相当）"""
    
    def __init__(self, repository: TodoRepository):
        self.repository = repository
    
    def get_all_todos(self) -> List[TodoResponse]:
        """すべてのTodoを取得"""
        todos = self.repository.get_all()
        return [self._convert_to_response(todo) for todo in todos]
    
    def get_todo_by_id(self, todo_id: int) -> Optional[TodoResponse]:
        """IDでTodoを取得"""
        todo = self.repository.get_by_id(todo_id)
        if todo:
            return self._convert_to_response(todo)
        return None
    
    def create_todo(self, todo_data: TodoCreate) -> TodoResponse:
        """新しいTodoを作成"""
        # ビジネスロジック: バリデーション
        if len(todo_data.title.strip()) == 0:
            raise ValueError("タイトルは必須です")
        
        # リポジトリ層に委譲
        todo = self.repository.create(todo_data)
        return self._convert_to_response(todo)
    
    def update_todo(self, todo_id: int, todo_data: TodoUpdate) -> Optional[TodoResponse]:
        """Todoを更新"""
        # ビジネスロジック: 存在チェック
        existing_todo = self.repository.get_by_id(todo_id)
        if not existing_todo:
            return None
        
        # ビジネスロジック: バリデーション
        if todo_data.title and len(todo_data.title.strip()) == 0:
            raise ValueError("タイトルは必須です")
        
        # リポジトリ層に委譲
        todo = self.repository.update(todo_id, todo_data)
        if todo:
            return self._convert_to_response(todo)
        return None
    
    def delete_todo(self, todo_id: int) -> bool:
        """Todoを削除"""
        # ビジネスロジック: 存在チェック
        existing_todo = self.repository.get_by_id(todo_id)
        if not existing_todo:
            return False
        
        # リポジトリ層に委譲
        return self.repository.delete(todo_id)
    
    def get_todos_by_tag(self, tag_name: str) -> List[TodoResponse]:
        """タグでTodoを検索"""
        todos = self.repository.get_by_tag(tag_name)
        return [self._convert_to_response(todo) for todo in todos]
    
    def toggle_todo_completion(self, todo_id: int) -> Optional[TodoResponse]:
        """Todoの完了状態を切り替え"""
        todo = self.repository.get_by_id(todo_id)
        if not todo:
            return None
        
        # ビジネスロジック: 完了状態の切り替え
        todo.completed = not todo.completed
        updated_todo = self.repository.save(todo)
        return self._convert_to_response(updated_todo)
    
    def _convert_to_response(self, todo: Todo) -> TodoResponse:
        """モデルをレスポンススキーマに変換"""
        return TodoResponse(
            id=todo.id,
            title=todo.title,
            description=todo.description,
            completed=todo.completed,
            tags=[{"id": tag.id, "name": tag.name, "color": tag.color} for tag in todo.tags],
            created_at=todo.created_at,
            updated_at=todo.updated_at
        )