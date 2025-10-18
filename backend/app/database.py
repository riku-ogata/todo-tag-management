# backend/app/database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# データベースURL
DATABASE_URL = os.getenv("DATABASE_URL", "mysql://todo_user:todo_password@mysql:3306/todo_manager")

# SQLAlchemyエンジンを作成
engine = create_engine(DATABASE_URL)

# セッションファクトリーを作成
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# ベースクラス
Base = declarative_base()

def get_db():
    """データベースセッションを取得する依存性注入関数"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
