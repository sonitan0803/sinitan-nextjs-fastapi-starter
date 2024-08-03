from fastapi import FastAPI
from api.routers  import users  # routersをインポート

app = FastAPI()

app.include_router(users.router)