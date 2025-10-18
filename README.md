# Todo Tag Manager

ToDo＋タグ管理アプリケーション - FastAPI + React + MySQL + Docker

## 🎯 プロジェクト概要

このプロジェクトは、タスクを登録し、完了・未完了・タグで管理できるWebアプリケーションです。本番運用とCI/CDの学習を目的として、Docker化された環境で開発します。

### 技術スタック
- **バックエンド**: FastAPI + Python 3.11
- **フロントエンド**: React + TypeScript + Material-UI
- **データベース**: MySQL 8.0
- **コンテナ**: Docker + Docker Compose
- **本番環境**: AWS (EC2, RDS, S3, CloudFront, Route53)

## 🚀 クイックスタート

### 前提条件
- Python 3.8以上
- Docker Desktop
- Git

### セットアップ手順

1. **リポジトリのクローン**
```bash
git clone https://github.com/yourusername/todo-tag-manager.git
cd todo-tag-manager
```

2. **Docker環境の起動**
```bash
docker-compose -f config/docker-compose.yml up -d
```

3. **動作確認**
```bash
# バックエンドAPI
curl http://localhost:8000

# フロントエンド
# ブラウザで http://localhost:3000 にアクセス
```

## 📁 プロジェクト構造

```
todo-tag-manager/
├── backend/                 # FastAPI バックエンド
│   ├── app/
│   │   ├── main.py          # FastAPIアプリのエントリーポイント
│   │   ├── models/          # データベースモデル
│   │   │   └── todo.py      # Todo・Tagモデル
│   │   ├── routers/         # API エンドポイント
│   │   ├── schemas/         # Pydantic スキーマ
│   │   ├── seeders/         # 初期データシーダー
│   │   │   └── initial_data.py
│   │   ├── database.py      # DB接続設定
│   │   └── config.py        # 設定ファイル
│   ├── alembic/             # マイグレーション管理
│   │   ├── versions/        # マイグレーションファイル
│   │   ├── env.py           # Alembic環境設定
│   │   └── script.py.mako   # マイグレーションテンプレート
│   ├── alembic.ini          # Alembic設定ファイル
│   ├── requirements.txt     # Python依存関係
│   ├── Dockerfile          # Docker設定
│   └── .env                # 環境変数
├── frontend/               # React フロントエンド
│   ├── src/
│   │   ├── components/     # React コンポーネント
│   │   ├── services/       # API 通信
│   │   ├── types/          # TypeScript型定義
│   │   ├── App.tsx         # メインコンポーネント
│   │   ├── App.css         # アプリケーションスタイル
│   │   └── index.css       # グローバルスタイル
│   ├── public/
│   │   └── index.html      # HTMLテンプレート
│   ├── package.json        # Node.js依存関係
│   ├── tsconfig.json       # TypeScript設定
│   ├── tailwind.config.js  # Tailwind CSS設定
│   ├── postcss.config.js   # PostCSS設定
│   ├── Dockerfile          # Docker設定
│   └── .env                # 環境変数
├── config/                 # 設定ファイル
│   ├── docker-compose.yml  # 開発環境
│   └── docker-compose.prod.yml # 本番環境
└── docs/                   # ドキュメント
    ├── README.md
    └── API.md
```

## 🛠️ 開発環境

### Docker Compose サービス

| サービス | ポート | 説明 |
|---------|-------|------|
| `backend` | 8000 | FastAPI バックエンド |
| `frontend` | 3000 | React フロントエンド |
| `mysql` | 3306 | MySQL データベース |

### 環境変数

#### バックエンド (.env)
```bash
DATABASE_URL=mysql://todo_user:todo_password@mysql:3306/todo_manager
SECRET_KEY=your-secret-key-here-change-in-production
DEBUG=True
CORS_ORIGINS=http://localhost:3000
```

#### フロントエンド (.env)
```bash
REACT_APP_API_URL=http://localhost:8000
REACT_APP_ENV=development
```

## 🔧 開発コマンド

### Docker Compose コマンド
```bash
# 全サービスを起動
docker-compose -f config/docker-compose.yml up -d

# 全サービスを停止
docker-compose -f config/docker-compose.yml down

# ログを確認
docker-compose -f config/docker-compose.yml logs

# 特定のサービスのログを確認
docker-compose -f config/docker-compose.yml logs backend
```

### 個別サービス起動
```bash
# バックエンド + MySQL
docker-compose -f config/docker-compose.yml up backend mysql

# フロントエンドのみ
docker-compose -f config/docker-compose.yml up frontend
```

## 📚 API エンドポイント

### タスク管理
- `GET /tasks` - タスク一覧取得
- `POST /tasks` - タスク作成
- `PUT /tasks/{id}` - タスク更新
- `DELETE /tasks/{id}` - タスク削除

### タグ管理
- `GET /tags` - タグ一覧取得
- `POST /tags` - タグ作成
- `PUT /tags/{id}` - タグ更新
- `DELETE /tags/{id}` - タグ削除

## 🗄️ データベース管理

### Sequel Ace での接続

Sequel Aceを使用してデータベースを視覚的に管理できます。

#### 接続設定
1. **Sequel Ace** を起動
2. **新しい接続を作成** (+ ボタンをクリック)
3. **接続情報を入力**:
   ```
   Connection Name: Todo Manager DB
   Host: 127.0.0.1
   Username: todo_user
   Password: todo_password
   Database: todo_manager
   Port: 3306
   ```
4. **接続をテスト** → **接続**

#### 管理者権限での接続
```
Connection Name: Todo Manager Root
Host: 127.0.0.1
Username: root
Password: rootpassword
Database: (空白のまま)
Port: 3306
```

### マイグレーション管理

FastAPIではAlembicを使用してデータベースのスキーマを管理します。

#### 新しいマイグレーションの作成
```bash
# モデル変更後にマイグレーションファイルを自動作成
docker exec todo_backend alembic revision --autogenerate -m "Add new column"

# 手動でマイグレーションファイルを作成
docker exec todo_backend alembic revision -m "Manual migration"
```

#### マイグレーションの実行
```bash
# 最新のマイグレーションを適用
docker exec todo_backend alembic upgrade head

# 特定のバージョンに移動
docker exec todo_backend alembic upgrade <revision_id>

# マイグレーション履歴を確認
docker exec todo_backend alembic history
```

#### テーブル・カラムの追加手順

1. **モデルファイルを編集** (`backend/app/models/todo.py`)
   ```python
   class Todo(Base):
       __tablename__ = 'todos'
       
       id = Column(Integer, primary_key=True, autoincrement=True)
       title = Column(String(255), nullable=False)
       description = Column(Text)
       completed = Column(Boolean, default=False)
       # 新しいカラムを追加
       priority = Column(String(20), default='medium')
       due_date = Column(DateTime)
       created_at = Column(DateTime, default=func.now())
       updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
   ```

2. **マイグレーションファイルを生成**
   ```bash
   docker exec todo_backend alembic revision --autogenerate -m "Add priority and due_date to todos"
   ```

3. **マイグレーションを実行**
   ```bash
   docker exec todo_backend alembic upgrade head
   ```

4. **Sequel Aceで確認**
   - テーブル構造の変更を確認
   - 新しいカラムが追加されていることを確認

#### シーダー（初期データ）の実行
```bash
# 初期データを作成
docker exec todo_backend python -c "from app.seeders.initial_data import create_initial_data; create_initial_data()"
```

## 🧪 テスト

### バックエンドテスト
```bash
# Dockerコンテナ内でテスト実行
docker exec -it todo_backend pytest
```

### フロントエンドテスト
```bash
# Dockerコンテナ内でテスト実行
docker exec -it todo_frontend npm test
```

## 🚀 デプロイ

### AWS デプロイ
```bash
# 本番環境用Docker Compose
docker-compose -f config/docker-compose.prod.yml up -d
```

### CI/CD
GitHub Actionsを使用した自動デプロイパイプラインが設定されています。

## 🐛 トラブルシューティング

### よくある問題

#### ポートが使用中
```bash
# 使用中のプロセスを確認
lsof -i :8000  # バックエンド用
lsof -i :3000  # フロントエンド用
lsof -i :3306  # MySQL用

# Dockerコンテナを停止
docker-compose down
```

#### コンテナが起動しない
```bash
# ログを確認
docker-compose logs

# 特定のサービスのログを確認
docker-compose logs backend
docker-compose logs frontend
docker-compose logs mysql
```

#### MySQL接続エラー
```bash
# MySQLに接続
docker exec -it todo_mysql mysql -u todo_user -ptodo_password todo_manager

# rootユーザーで接続
docker exec -it todo_mysql mysql -u root -prootpassword
```

#### Sequel Ace接続エラー
```bash
# MySQLコンテナの状態確認
docker ps | grep mysql

# MySQLのログを確認
docker logs todo_mysql

# ポート3306が開いているか確認
lsof -i :3306
```

#### マイグレーションエラー
```bash
# マイグレーション履歴を確認
docker exec todo_backend alembic history

# 現在のマイグレーション状態を確認
docker exec todo_backend alembic current

# マイグレーションをリセット（注意：データが失われます）
docker exec todo_backend alembic downgrade base
docker exec todo_backend alembic upgrade head

# マイグレーションファイルを手動で編集
# backend/alembic/versions/ 内のファイルを確認
```

## 🤝 コントリビューション

1. このリポジトリをフォーク
2. フィーチャーブランチを作成 (`git checkout -b feature/amazing-feature`)
3. 変更をコミット (`git commit -m 'Add some amazing feature'`)
4. ブランチにプッシュ (`git push origin feature/amazing-feature`)
5. プルリクエストを作成

**Happy Coding! 🚀**
