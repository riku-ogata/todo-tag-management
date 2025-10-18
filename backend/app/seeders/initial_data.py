# backend/app/seeders/initial_data.py
from sqlalchemy.orm import Session
from app.models.todo import Tag, Todo, todo_tags
from app.database import get_db

def create_initial_data():
    """初期データを作成するシーダー関数"""
    db = next(get_db())
    
    try:
        # タグの作成
        tags_data = [
            {"name": "仕事", "color": "#EF4444"},
            {"name": "プライベート", "color": "#10B981"},
            {"name": "学習", "color": "#3B82F6"},
            {"name": "緊急", "color": "#F59E0B"},
        ]
        
        created_tags = []
        for tag_data in tags_data:
            existing_tag = db.query(Tag).filter(Tag.name == tag_data["name"]).first()
            if not existing_tag:
                tag = Tag(**tag_data)
                db.add(tag)
                created_tags.append(tag)
            else:
                created_tags.append(existing_tag)
        
        db.commit()
        
        # Todoの作成
        todos_data = [
            {
                "title": "プロジェクトの企画書作成",
                "description": "来週のプレゼンに向けて企画書を作成する",
                "completed": False,
                "tag_names": ["仕事", "緊急"]
            },
            {
                "title": "買い物リスト作成",
                "description": "週末の買い物のためのリストを作成",
                "completed": False,
                "tag_names": ["プライベート"]
            },
            {
                "title": "Reactの学習",
                "description": "HooksとState管理について学習する",
                "completed": True,
                "tag_names": ["学習"]
            },
        ]
        
        for todo_data in todos_data:
            tag_names = todo_data.pop("tag_names")
            existing_todo = db.query(Todo).filter(Todo.title == todo_data["title"]).first()
            
            if not existing_todo:
                todo = Todo(**todo_data)
                db.add(todo)
                db.flush()  # IDを取得するためにflush
                
                # タグとの関連付け
                for tag_name in tag_names:
                    tag = next((t for t in created_tags if t.name == tag_name), None)
                    if tag:
                        todo.tags.append(tag)
        
        db.commit()
        print("✅ 初期データの作成が完了しました！")
        
    except Exception as e:
        db.rollback()
        print(f"❌ 初期データの作成に失敗しました: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    create_initial_data()
