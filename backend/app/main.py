from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import todos

app = FastAPI(title="Todo Tag Manager API")

# CORS設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ルーターを登録（Laravelのweb.phpに相当）
app.include_router(todos.router)

@app.get("/")
async def root():
    return {"message": "Todo Tag Manager API", "status": "running"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}