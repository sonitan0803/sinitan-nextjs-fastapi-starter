from fastapi import APIRouter

router = APIRouter()

@router.get("/api/python",tags=["users"])
async def read_user_me():
    return {"this": "test"}